import os
import datetime

class Todo:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_id):
        self.tasks.pop(task_id)
        self.save_tasks()

    def complete_task(self, task_id):
        self.tasks[task_id]['completed'] = True
        self.save_tasks()

    def save_tasks(self):
        with open('tasks.txt', 'w') as f:
            for task in self.tasks:
                f.write(f"{task['description']}|{task['completed']}\n")

    def load_tasks(self):
        if os.path.exists('tasks.txt'):
            with open('tasks.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    description, completed = line.strip().split('|')
                    self.tasks.append({'description': description, 'completed': completed == 'True'})

    def print_tasks(self):
        for i, task in enumerate(self.tasks):
            completed = '(x)' if task['completed'] else ' '
            print(f"{i}. {completed} {task['description']}")

    def run(self):
        while True:
            print("\nTo-Do List")
            self.print_tasks()
            print("\n1. Add Task")
            print("2. Remove Task")
            print("3. Complete Task")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                task = input("Enter task description: ")
                self.add_task({'description': task, 'completed': False})
            elif choice == '2':
                task_id = int(input("Enter task number: "))
                self.remove_task(task_id)
            elif choice == '3':
                task_id = int(input("Enter task number: "))
                self.complete_task(task_id)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Todo().run()