from pathlib import Path
import sys
import json
from datetime import datetime

Task = dict[
    "id": int,
    "title": str,
    "description": str,
    "status": str,
    "created_at": str,
    "updated_at": str
]


class DB:
    def create_db(self):
        try:
            self.db_path = Path("./db/db.json")
            if not self.db_path.exists():
                self.db_path.write_text("[]")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    updated_at: str

class DB:
    def create_db(self):
        try:
            self.db_path = Path("./db/db.json")
            if not self.db_path.exists():
                self.db_path.write_text("[]")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

class TaskCLI:
    def __init__(self):
        self.db = DB()
        try:
            self.db.create_db()
            self.load_tasks()
            if len(self.tasks) == 0:
                self.add_task({
                    "id": 1,
                    "title": "First Task", 
                    "description": "First Task Description", 
                    "status": "in-progress",
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def load_tasks(self):
        try:
            with open(self.db.db_path, "r") as f:
                self.tasks = json.load(f)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def save_tasks(self):
        try:
            with open(self.db.db_path, "w") as f:
                json.dump(self.tasks, f, indent=4)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    def add_task(self, task: Task):
        try:
            self.tasks.append(task)
            self.save_tasks()
            print(f"Task {task['title']} added successfully")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def list_tasks(self, id: int = None, status: str = None):
        try:
            if id:
                tasks = [task for task in self.tasks if task['id'] == id]
            elif status:
                tasks = [task for task in self.tasks if task['status'] == status]
            else:
                tasks = self.tasks
            for task in tasks:
                print(f"ID: {task['id']}")
                print(f"Title: {task['title']}")
                print(f"Description: {task['description']}")
                print(f"Status: {task['status']}")
                print(f"Created At: {task['created_at']}")
                print(f"Updated At: {task['updated_at']}")
                print("-" * 20)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def update_task(self, task_id: int, title: str = None, description: str = None, status: str = None):
        try:
            if not title and not description and not status:
                print("Please provide at least one field to update")
                return
            task = next((task for task in self.tasks if task['id'] == task_id), None)
            if not task:
                print(f"Task {task_id} not found")
                return
            if title:
                task['title'] = title
            if description:
                task['description'] = description
            if status:
                task['status'] = status
            task['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_tasks()
            print(f"Task {task_id} updated successfully")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def delete_task(self, task_id: int):
        try:
            task = next((task for task in self.tasks if task['id'] == task_id), None)
            if not task:
                print(f"Task {task_id} not found")
                return
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Task {task_id} deleted successfully")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)