"""
This module provides the command-line interface for the task_cli application.
"""

import argparse
import sys
from datetime import datetime

from task_cli.core import TaskCLI
from task_cli.utils import get_config_file, print_config

def main():
    parse = argparse.ArgumentParser(description="Task CLI")
    parse.add_argument("-v", "--version", action="version", version=print_config())
    parse.add_argument("-c", "--config", action="store_true", help="Print config")
    parse.add_argument("-l", "--list", action="store_true", help="List tasks")
    parse.add_argument("-a", "--add", action="store_true", help="Add task")
    parse.add_argument("-u", "--update", action="store_true", help="Update task")
    parse.add_argument("-d", "--delete", action="store_true", help="Delete task")
    parse.add_argument("-t", "--title", type=str, help="Task title")
    parse.add_argument("-desc", "--description", type=str, help="Task description")
    parse.add_argument("-s", "--status", type=str, help="Task status")
    parse.add_argument("-i", "--id", type=int, help="Task id")
    parse.add_argument("-mip", "--mark-in-progress", action="store_true", help="Mark task as in progress")
    parse.add_argument("-md", "--mark-done", action="store_true", help="Mark task as done")
    subparsers = parse.add_subparsers(dest="command")
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', type=str, help='Task status')
    args = parse.parse_args()

    if args.config:
        print_config()
        return

    task_cli = TaskCLI()

    if args.list:
        task_cli.list_tasks()
    elif args.add:
        task_cli.add_task({
            "id": task_cli.tasks[-1]["id"] + 1 if task_cli.tasks else 1,
            "title": args.title, 
            "description": args.description, 
            "status": args.status or "in-progress",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    elif args.update:
        task_cli.update_task(args.id, title=args.title, description=args.description, status=args.status)
    elif args.delete:
        task_cli.delete_task(args.id)
    elif args.mark_in_progress:
        task_cli.update_task(args.id, status="in-progress")
    elif args.mark_done:
        task_cli.update_task(args.id, status="completed")
    elif args.command == 'list':
        task_cli.list_tasks(status=args.status)
    else:
        print("No action specified")