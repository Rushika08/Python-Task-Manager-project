import json
import logging
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

logging.basicConfig(filename='task_manager.log', level=logging.INFO)

class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Task Manager")

        self.tasks = []
        self.load_tasks()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Task Manager", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(self.master, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        for task in self.tasks:
            self.listbox.insert(tk.END, f"{task['name']} - Due: {task['due_date']} - Completed: {task['completed']}")

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.sort_button = tk.Button(self.master, text="Sort by Due Date", command=self.sort_tasks_by_due_date)
        self.sort_button.pack(side=tk.LEFT, padx=10)

        self.upcoming_button = tk.Button(self.master, text="Show Upcoming Tasks", command=self.show_upcoming_tasks)
        self.upcoming_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        try:
            name = simple_input("Enter task name:")
            description = simple_input("Enter task description:")
            due_date_str = simple_input("Enter due date (YYYY-MM-DD):")

            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

            task = {"name": name, "description": description, "due_date": due_date_str, "completed": False}
            self.tasks.append(task)
            self.listbox.insert(tk.END, f"{task['name']} - Due: {task['due_date']} - Completed: {task['completed']}")
            self.save_tasks()

            logging.info(f"Task added: {task}")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            task = self.tasks.pop(selected_index)
            self.listbox.delete(selected_index)
            self.save_tasks()

            logging.info(f"Task deleted: {task}")
        except IndexError:
            messagebox.showerror("Error", "Please select a task to delete.")

    def sort_tasks_by_due_date(self):
        self.tasks.sort(key=lambda x: datetime.strptime(x['due_date'], "%Y-%m-%d"))
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, f"{task['name']} - Due: {task['due_date']} - Completed: {task['completed']}")
        self.save_tasks()

        logging.info("Tasks sorted by due date.")

    def show_upcoming_tasks(self):
        today = datetime.now()
        upcoming_tasks = [task for task in self.tasks if not task['completed'] and datetime.strptime(task['due_date'], "%Y-%m-%d") >= today]

        if upcoming_tasks:
            messagebox.showinfo("Upcoming Tasks", "\n".join([f"{task['name']} - Due: {task['due_date']}" for task in upcoming_tasks]))
        else:
            messagebox.showinfo("Upcoming Tasks", "No upcoming tasks.")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            logging.warning("No tasks found.")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=2)

def simple_input(prompt):
    return simpledialog.askstring("Input", prompt)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
