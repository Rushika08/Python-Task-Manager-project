"""

Project Name        : Task Manager Project
Name                : Ashen Rushika David Jayasinghe
Github Username     : Rushika08
edX username        : Rushika_D
Country             : Sri Lanka
City                : Katunayake, Gampaha District
Date of recording   : 3rd January 2024

"""


import json
from datetime import datetime, timedelta
from prettytable import PrettyTable

def main():
    print("\n\nWelcome to Task Manager!")
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n"
              "4. Delete Task\n5. Sort Tasks by Due Date\n6. Show Upcoming Tasks\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            sort_tasks_by_due_date()
        elif choice == '6':
            show_upcoming_tasks()
        elif choice == '7':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        user_input = input("\nPress Enter to continue or input '7' to exit...\n")

        if user_input == '7':
            print("\nExiting Task Manager. Goodbye!")
            break

def add_task():
    task_name = input("Enter task name: ")
    description = input("Enter task description: ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    task = {
        "name": task_name,
        "description": description,
        "due_date": due_date_str,
        "completed": False
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        table = PrettyTable()
        table.field_names = ["Index", "Task Name", "Description", "Due Date", "Completed"]

        for index, task in enumerate(tasks, start=1):
            table.add_row([index, task['name'], task['description'], task['due_date'], task['completed']])

        print(table)

def mark_task_completed():
    tasks = load_tasks()
    view_tasks()

    try:
        task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        task_index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def sort_tasks_by_due_date():
    tasks = load_tasks()
    incomplete_tasks = [task for task in tasks if not task['completed']]

    if incomplete_tasks:
        incomplete_tasks.sort(key=lambda x: datetime.strptime(x['due_date'], "%Y-%m-%d"))
        save_tasks(incomplete_tasks)
        print("Tasks sorted by due date.")
    else:
        print("No incomplete tasks to sort.")

def show_upcoming_tasks():
    tasks = load_tasks()
    if tasks:
        today = datetime.now()
        upcoming_tasks = [task for task in tasks if not task['completed'] and datetime.strptime(task['due_date'], "%Y-%m-%d") >= today]
        if upcoming_tasks:
            table = PrettyTable()
            table.field_names = ["Index", "Task Name", "Due Date", "Completed"]

            for index, task in enumerate(upcoming_tasks, start=1):
                table.add_row([index, task['name'], task['due_date'], task['completed']])

            print(table)
        else:
            print("No upcoming tasks.")
    else:
        print("No tasks found.")

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

if __name__ == "__main__":
    main()
