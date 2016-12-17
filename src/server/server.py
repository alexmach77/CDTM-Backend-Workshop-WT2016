#!/usr/bin/env python
# coding: utf8

from flask import Flask, send_file, jsonify, request
import sys

from task import Task
from list import List
from utils import json_abort



# allow special characters (e.g. üäö ...)
reload(sys)
sys.setdefaultencoding('utf-8')

VERSION = 2.0

myLists = [
    List('Inbox', id='0'),
    List('Groceries', id='1')
]
myTasks = [
    Task('Think about lunch', '1', id='0', status = Task.COMPLETED),
    Task('Become a pro in backend development', '0', id='1', status= Task.NORMAL),
    Task('CONQUER THE WORLD!', '0', id='2', status = Task.NORMAL)
]

# Note: Setting static_url_path to '' has the following effect:
#   - Whenever a file is requested and there is no matching route defined
#     the flask server will look whether the file is in the 'static/' folder
#   - As a consequence, everyone can remotely access files within 'static/'
#   - We need this, so that the front-end works properly.
app = Flask(__name__, static_url_path='')

# MARK: Static routes
@app.route('/', methods=['GET'])
def frontEnd():
    return send_file('static/index.html')

# MARK: General routes
@app.route('/api/version', methods=['GET'])
def get_version():
    return jsonify({'version': VERSION})

# MARK: List routes
@app.route('/api/lists', methods=['GET'])
def get_lists():
    response = {}
    response['lists'] = [l.__dict__ for l in myLists]
    return jsonify(response)

# MARK: Task routes
@app.route('/api/lists/<string:list_id>/tasks', methods=['GET'])
def get_tasks(list_id):
    response = {}
    response['tasks'] = [t.__dict__ for t in myTasks if t.list==list_id]
    return jsonify(response)

#Create Task
@app.route('/api/lists/<string:list_id>/tasks', methods=['POST'])
def create_tasks(list_id):
    # 1. list_id does not exist.
    matching_list = [l for l in myLists if l.id == list_id]
    if len(matching_list) == 0:
        json_abort(400, "List does not exist")


    # 2. missing title. I need to get the title from the request
    data = request.get_json(force=True)
    print data["title"]
    # 3. Calculate the next task id. Need to get title and id in order to create a new task.
    #myTasks.append(Task('Think about lunch', list_id, id='0'))


    return "hello"




if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)
