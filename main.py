import argparse
import datetime
from Task import Task
from Tasks import Tasks


def main():
    # create an instance of Tasks
    all_tasks = Tasks()

    parser = argparse.ArgumentParser()
    # arguments for add
    parser.add_argument('--add', type=str, required=False, help='a task string to add to your list')
    parser.add_argument('--due', type=str, required=False, help='due date in dd/MM/YYYY format')
    parser.add_argument('--priority', type=int, required=False, default=1, help='priority of tasks; default value is 1')
    # arguments for query
    parser.add_argument('--query', required=False, type=str, nargs='+', help="priority of task; default value is 1")
    # arguments for done
    parser.add_argument('--done', type=int, required=False)
    # arguments for delete
    parser.add_argument('--delete', type=int)
    # for list and report, optional positional arguments
    parser.add_argument('--list', action='store_true', required=False, help='list all tasks that have not been completed')
    parser.add_argument('--report', action='store_true', required=False, help='list all tasks')      # error: calling the report function goes into list

    args = parser.parse_args()

    if args.add:
        if args.due:    # checked
            all_tasks.add(args.add, args.priority, args.due)
        else:
            all_tasks.add(args.add, args.priority)

    elif args.done:   # checked
        all_tasks.done(args.done)

    elif args.delete:   # checked
        all_tasks.delete(args.delete)

    elif args.list:   # CHECKED
        all_tasks.list()

    elif args.report:
        all_tasks.report()

    elif args.query:
        all_tasks.query(args.query)

    # call pickle_tasks at the end and exit the program
    all_tasks.pickle_tasks()


main()