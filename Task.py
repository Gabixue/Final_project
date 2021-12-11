import itertools
import datetime


class Task:


    def __init__(self, name, priority, id, due_date=None, completed=None):
        self.created = datetime.date.today()
        # self.id = next(Task.newId)+1
        self.id = id
        self.name = name
        self.priority = priority

        if due_date:
            # self.due_date = datetime.datetime.strptime(due_date, '%m/%d/%Y').date()
            self.due_date = datetime.datetime.strptime(due_date, '%m/%d/%Y')
        else:
            self.due_date = None

        if completed:
            self.completed = completed
        else:
            self.completed = None
