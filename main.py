import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import json


class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.load_tasks()

        # Style configuration
        self.style = ttk.Style()
        self.style.configure("TButton", font=('Helvetica', 10), padding=5)
        self.style.configure("TLabel", font=('Helvetica', 10))
        self.style.configure("TEntry", font=('Helvetica', 10), padding=5)
        self.style.configure("TOptionMenu", font=('Helvetica', 10))

        # Create the UI components
        self.create_widgets()
        self.update_task_list()

    def create_widgets(self):
        self.task_entry = ttk.Entry(self.root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.priority_var = tk.StringVar(value='medium')
        ttk.Label(self.root, text="Priority:").grid(row=0, column=2)
        ttk.OptionMenu(self.root, self.priority_var, 'medium', 'high', 'medium', 'low').grid(row=0, column=3)

        self.due_date_entry = ttk.Entry(self.root, width=15)
        self.due_date_entry.grid(row=0, column=4, padx=10, pady=10)
        self.due_date_entry.insert(0, 'YYYY-MM-DD')

        self.add_task_button = ttk.Button(self.root, text="Add Task", command=self.add_task, style="Accent.TButton")
        self.add_task_button.grid(row=0, column=5, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=75, height=20, font=('Helvetica', 10))
        self.task_listbox.grid(row=1, column=0, columnspan=6, padx=10, pady=10)
        self.task_listbox.bind('<Double-Button-1>', self.complete_task)

        self.edit_task_button = ttk.Button(self.root, text="Edit Task", command=self.edit_task, style="Accent.TButton")
        self.edit_task_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_task_button = ttk.Button(self.root, text="Delete Task", command=self.delete_task,
                                             style="Accent.TButton")
        self.delete_task_button.grid(row=2, column=1, padx=10, pady=10)

        self.save_button = ttk.Button(self.root, text="Save Tasks", command=self.save_tasks, style="Accent.TButton")
        self.save_button.grid(row=2, column=2, padx=10, pady=10)

        self.exit_button = ttk.Button(self.root, text="Exit", command=self.exit_application, style="Accent.TButton")
        self.exit_button.grid(row=2, column=3, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        due_date = self.due_date_entry.get()

        if not task:
            messagebox.showwarning("Input Error", "Please enter a task.")
            return

        if priority not in ['high', 'medium', 'low']:
            messagebox.showwarning("Input Error", "Invalid priority. Must be 'high', 'medium', or 'low'.")
            return

        if due_date:
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                messagebox.showwarning("Input Error", "Invalid date format. Use YYYY-MM-DD.")
                return

        self.tasks.append({'task': task, 'completed': False, 'priority': priority, 'due_date': due_date})
        self.update_task_list()
        self.task_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.due_date_entry.insert(0, 'YYYY-MM-DD')

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            status = "completed" if task['completed'] else "Not completed"
            priority = task.get('priority', 'medium')
            due_date = task['due_date'] if task['due_date'] else "No due date"
            task_str = f"{index}. {task['task']} - {status} - Priority: {priority} - Due: {due_date}"
            self.task_listbox.insert(tk.END, task_str)

    def complete_task(self, event):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]['completed'] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to complete.")

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if not new_task:
                messagebox.showwarning("Input Error", "Please enter a task.")
                return
            self.tasks[selected_index]['task'] = new_task
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def save_tasks(self, filename='tasks.json'):
        with open(filename, 'w') as f:
            json.dump(self.tasks, f)

    def load_tasks(self, filename='tasks.json'):
        try:
            with open(filename, 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def exit_application(self):
        self.save_tasks()
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()
