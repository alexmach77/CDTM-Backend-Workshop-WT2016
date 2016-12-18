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


## Objects in memory

if I print my object a get an addreess in my memory 0xdersijio293. Here is the object loction. Which will have some attribute and methods store in that address. The content in ecah memory address u have the attributes. 

If I have task2=task, then the new task2 will also point to the same address of task1. Hence if i change task2 i will also change task 1.

The only way to avoid it, is to create a new object for task2 and then give it the values of task1.



##Databases


when we create the object we store them in memory. In variables, but when we restart the server, all of them are gone.
Hence we need a DB to store the Data in orgnzed way.


RDBMS cpmply to the ACID model (atomicity, consistency, isolation, durability). These are the reasons why to use it instead of excel or text file.


- Atomicity: the row is writen or not. Tne data is obtained or not. u cannot get half row.

- Consistency: The DB 

- Isolation: Different clients can access the db as thought there were only one instance/client accesing it. They never notice that somebody else is working in the db

- Durability: Non-volatile storage, is persistent storage. Power outage is not a problem.



#SQL important flags

on delete cascade.
If I delete an user in the table USERS, i want that all his tweets to be deleted.  Hence i use on delete ascade when defininig the tweets.


##Sql injection
in oython we use placeholders to pass variables in querryes and we do it in the execute statemet. If we do it in the query statement anybody can send a code inside a variable and drop all the DB.

But if we do it in the execute statemetn, then python takes care that this do not happen.


##Python dictionaries
dict.get is one of the many built-in functions of the dictionaries. It returns the value for the given key.

dict.get(key, default=None)
	
	def dict_from_row(row):
	    ''' Converts a query result into a dict '''
	    return {} if row == None else dict(zip(row.keys(), row))


    cookieTypes = []
    for row in cur:
        cookieTypes.append(dict_from_row(row).get('type'))
    return cookieTypes

