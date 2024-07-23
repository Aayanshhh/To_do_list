# To-Do List Application

A command-line to-do list application implemented in Python, enhanced with features like task prioritization, due dates, editing, deleting tasks, and data persistence.

## Features

- **User Interface Enhancements**: Colorful and intuitive command-line interface using `colorama`.
- **Task Prioritization**: Ability to set task priority (high, medium, low).
- **Due Dates**: Set due dates for tasks and view them in the task list.
- **Edit Tasks**: Edit existing tasks.
- **Delete Tasks**: Delete tasks from the list.
- **Data Persistence**: Save tasks to a JSON file and load them on startup.


## Usage

### Main Menu

The main menu provides the following options:

1. Add a task
2. View tasks
3. Complete a task
4. Edit a task
5. Delete a task
6. Exit

### Adding a Task

- You will be prompted to enter the task description.
- You will be prompted to enter the task priority (high, medium, low).
- You will be prompted to enter the due date (optional, in YYYY-MM-DD format).

### Viewing Tasks

- Displays all tasks with their status (completed/not completed), priority, and due date.

### Completing a Task

- You will be prompted to enter the task number to mark as completed.

### Editing a Task

- You will be prompted to enter the task number to edit.
- You will be prompted to enter the new task description.

### Deleting a Task

- You will be prompted to enter the task number to delete.

### Exiting the Application

- Saves the tasks to a JSON file (`tasks.json`) and exits the application.

## Example

```bash
To-Do List Menu:
1. Add a task
2. View tasks
3. Complete a task
4. Edit a task
5. Delete a task
6. Exit
Choose an option: 1
Enter a new task: Buy groceries
Enter priority (high, medium, low): high
Enter due date (YYYY-MM-DD) or leave blank: 2023-12-31
Added task: 'Buy groceries' with priority 'high' and due date '2023-12-31'
