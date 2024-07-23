from colorama import Fore, Style, init
import json
from datetime import datetime

init(autoreset=True)

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task, priority='medium', due_date=None):
        if priority not in ['high', 'medium', 'low']:
            print(Fore.RED + "Invalid priority. Must be 'high', 'medium', or 'low'.")
            return

        if due_date:
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                print(Fore.RED + "Invalid date format. Use YYYY-MM-DD.")
                return

        self.tasks.append({'task': task, 'completed': False, 'priority': priority, 'due_date': due_date})
        print(Fore.GREEN + f"Added task: '{task}' with priority '{priority}' and due date '{due_date}'")

    def view_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + "No tasks in the to-do list.")
            return

        for index, task in enumerate(self.tasks, start=1):
            status = Fore.GREEN + "completed" if task['completed'] else Fore.RED + "Not completed"
            priority = task.get('priority', 'medium')
            due_date = task['due_date'] if task['due_date'] else "No due date"
            print(f"{index}. {task['task']} - {status} - Priority: {priority} - Due: {due_date}")

    def complete_task(self, task_number):
        if not isinstance(task_number, int) or task_number <= 0 or task_number > len(self.tasks):
            print(Fore.RED + "Invalid task number.")
            return

        self.tasks[task_number - 1]['completed'] = True
        print(Fore.GREEN + f"Marked task {task_number} as completed.")

    def edit_task(self, task_number, new_task):
        if not isinstance(task_number, int) or task_number <= 0 or task_number > len(self.tasks):
            print(Fore.RED + "Invalid task number.")
            return

        self.tasks[task_number - 1]['task'] = new_task
        print(Fore.GREEN + f"Edited task {task_number}.")

    def delete_task(self, task_number):
        if not isinstance(task_number, int) or task_number <= 0 or task_number > len(self.tasks):
            print(Fore.RED + "Invalid task number.")
            return

        del self.tasks[task_number - 1]
        print(Fore.GREEN + f"Deleted task {task_number}.")

    def save_tasks(self, filename='tasks.json'):
        with open(filename, 'w') as f:
            json.dump(self.tasks, f)

    def load_tasks(self, filename='tasks.json'):
        try:
            with open(filename, 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def run(self):
        while True:
            print(Fore.CYAN + "\nTo-Do List Menu:")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Complete a task")
            print("4. Edit a task")
            print("5. Delete a task")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                task = input("Enter a new task: ")
                priority = input("Enter priority (high, medium, low): ")
                due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
                due_date = due_date if due_date else None
                self.add_task(task, priority, due_date)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                try:
                    task_number = int(input("Enter the task number to complete: "))
                    self.complete_task(task_number)
                except ValueError:
                    print(Fore.RED + "Please enter a valid number.")
            elif choice == '4':
                try:
                    task_number = int(input("Enter the task number to edit: "))
                    new_task = input("Enter the new task: ")
                    self.edit_task(task_number, new_task)
                except ValueError:
                    print(Fore.RED + "Please enter a valid number.")
            elif choice == '5':
                try:
                    task_number = int(input("Enter the task number to delete: "))
                    self.delete_task(task_number)
                except ValueError:
                    print(Fore.RED + "Please enter a valid number.")
            elif choice == '6':
                print(Fore.CYAN + "Exiting the to-do list application.")
                self.save_tasks()
                break
            else:
                print(Fore.RED + "Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
