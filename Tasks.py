import pickle
import argparse
import datetime
from Task import Task
import os.path


class Tasks:
    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = []

        # if the file exists, load into a list
        if os.path.exists('.todo.pickle'):
            f = open('.todo.pickle', 'rb')
            try:
                self.tasks = pickle.load(f)
            except EOFError:
                self.tasks = []
            f.close()

        # if the file does not exist, create it
        else:
            open('.todo.pickle', 'w')

        # sort the list by creation date
        self.tasks.sort(key=lambda x: x.created)

    def pickle_tasks(self):   # use at the end of main
        """Pickle your task list to a file"""
        f = open('.todo.pickle', 'wb')
        pickle.dump(self.tasks, f)
        f.close()

    def list(self):
        not_completed = []
        for t in self.tasks:
            if not t.completed:
                not_completed.append(t)

        has_due_date = []
        no_due_date = []
        for t in not_completed:
            if t.due_date:
                has_due_date.append(t)
            else:
                no_due_date.append(t)

        # sort the list that has due date by due date and then by priority in the case of same due date
        has_due_date.sort(key=lambda x: (x.due_date, x.priority), reverse=True)
        # sort the list that has no due date by priority
        no_due_date.sort(key=lambda x: x.priority)

        print('ID   Age  Due Date   Priority   Task')
        print('--   ---  --------   --------   ----')
        today = datetime.date.today()

        for t in has_due_date:
            age = (today - t.created).days
            print(str(t.id) + '    ' + str(age) + 'd' + '   ' + datetime.datetime.strftime(t.due_date, '%m/%d/%Y') + '  ' + str(
                t.priority) + '         ' + t.name)

        for t in no_due_date:
            age = (today - t.created).days
            print(str(t.id) + '    ' + str(age) + 'd' + '   ' + '-        ' + '   ' + str(
                t.priority) + '         ' + t.name)

    def report(self):  # checked, still has to change datetime format
        has_due_date = []
        no_due_date = []
        for t in self.tasks:
            if t.due_date:
                has_due_date.append(t)
            else:
                no_due_date.append(t)

        # sort the list that has due date by due date and then by priority in the case of same due date
        has_due_date.sort(key=lambda x: (x.due_date, x.priority), reverse=True)
        # sort the list that has no due date by priority
        no_due_date.sort(key=lambda x: x.priority)

        print('ID   Age  Due Date   Priority   Task                Created                       Completed')
        print('--   ---  --------   --------   ----                ---------------------------   -------------------------')
        today = datetime.date.today()

        for t in has_due_date:
            age = (today - t.created).days

            if t.completed:
                completed = t.completed
            else:
                completed = '-'

            print(str(t.id) + '    ' + str(age) + 'd' + '   ' + datetime.datetime.strftime(t.due_date, '%m/%d/%Y') + '  ' + str(
                t.priority) + '         ' + t.name + '                 ' + datetime.datetime.strftime(t.created,
                                                                                                    '%m/%d/%Y')
                  + '                    ' + completed)

        for t in no_due_date:
            age = (today - t.created).days

            if t.completed:
                completed = t.completed
            else:
                completed = '-'

            print(str(t.id) + '    ' + str(age) + 'd' + '   ' + '-        ' + '   ' + str(
                t.priority) + '         ' + t.name + '            ' + datetime.datetime.strftime(t.created,
                                                                                                 '%m/%d/%Y') + '                    ' + completed)

    def done(self, id):   # checked
        for t in self.tasks:
            if id == t.id:
                t.completed = datetime.date.today().strftime('%m/%d/%Y')
                print('Completed task', t.id)
                break


    def query(self, query_list):    # checked
        print('ID   Age  Due Date   Priority   Task')
        print('--   ---  --------   --------   ----')

        today = datetime.date.today()
        for t in self.tasks:
            # make sure only not completed tasks are shown
            if not t.completed:
                # iterate over all search terms that are passed in
                for word in query_list:
                    if word in t.name:
                        age = (today - t.created).days

                        if t.due_date:
                            print(str(t.id) + '    ' + str(age) + 'd' + '   ' + t.due_date.strftime(
                                '%m/%d/%Y') + ' ' + str(
                                t.priority) + '          ' + t.name)
                        else:
                            print(str(t.id) + '    ' + str(age) + 'd' + '   ' + '-' + '          ' + str(
                                t.priority) + '          ' + t.name)

    def add(self, name, priority, due_date=None):

        # checking for valid input
        if not isinstance(name, str):
            print('1There was an error in creating your task. Run "todo -h" for usage instructions.')
            exit()

        if due_date and not isinstance(due_date, str):
            print('2There was an error in creating your task. Run "todo -h" for usage instructions.')
            exit()

        if not isinstance(priority, int):
            print('3There was an error in creating your task. Run "todo -h" for usage instructions.')
            exit()

        # create an instance of the task
        t = Task(name, priority, due_date)
        self.tasks.append(t)
        print('Created task', t.id)
        # print(self.tasks)

    def delete(self, id):   # checked
        for t in self.tasks:
            if t.id == id:
                self.tasks.remove(t)
                print('Deleted task', t.id)
                break
