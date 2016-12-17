##backend workshop notes
###REST Representtional state transfer
75% use rest.


http is the unerlying protocol of all apis

get: get data from server

post: send new data to the server

put updates an existing resource

patch: changes single propoerties in the server


4XX client error. Ex 402. (something u sent to ther server was not right)
5xx server error
2xx success! =)



@app.route('/version', methods=['GET'])
def version():
    d = {'version_number': 'Version 2.22'}
    return flask.jsonify(**d)

##List or dictionary comprehension is really useful.
A lot of functionality in one line.
For every task check if the id belongs is equal to list_id, if so, then add them to an array, which is going to be saved in a hash for the key 'tasks'.

    response['tasks'] = [t.__dict__ for t in myTasks if t.list==list_id]


##Example how i do it vs doing with list comprehension
How I do it:

    #2. Delete task
    for task in myTasks:
        if task.id == task_id:
            myTasks.remove(task)
    print [t.id for t in myTasks]
    return jsonify({'result': True})

How it should be: 

    # 2. Check whether the specified task exists
    tasks = [t for t in myTasks if t.id == task_id and t.list == list_id]
    myTasks.remove(tasks[0])

    return jsonify({'result': True})
