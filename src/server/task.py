class Task():

    def __init__(self, id, title, list_id,status,description,due,revision):
        self.id = id
        self.title = title
        self.revision = list_id
        self.status = status
        self.description = description
        self.due = due
        self.revision = revision
