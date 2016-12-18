class Task:
    """Represents one Todo-Item"""
<<<<<<< HEAD
    
    NORMAL = 'normal'
    COMPLETED = 'completed'

    def __init__(self, title, list, id='', status = NORMAL, description = '', due = '', revision = 1):
        self.id = id
        self.list = list
        self.title =  title
=======

    NORMAL = 'normal'
    COMPLETED = 'completed'

    def __init__(self, title, list, id='', status=NORMAL, description='', due='', revision=1):
        self.id = id
        self.list = list
        self.title = title
>>>>>>> be3dccf26ae483a109e2ebbd212e0ac55e4d2c73
        self.status = status
        self.description = description
        self.due = due
        self.revision = revision
