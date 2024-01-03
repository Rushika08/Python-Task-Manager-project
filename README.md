# **Task Manager Project**

#### Video Demo:  <URL HERE>
#### Description:

## Overview
The Task Manager project is a command-line-based application designed to assist users in organizing and managing their tasks efficiently. Developed in Python, this project provides a user-friendly interface for different tasks. Such as,
* Add tasks
* View tasks
* Mark completed tasks
* Delete tasks
* Sort tasks by due date
* Show upcoming tasks

## Features
# **1. Add Task**

Users can easily add tasks to the manager by providing essential information such as task name, description, and due date. The application validates the due date format to ensure accurate entry. The task description is not essential to provide.

# **2. View Tasks**

The project enables users to view their tasks, presenting them in a well-organized tabular format. The table includes key details like task name, description, due date, and completion status.

# **3. Mark Task as Completed**

Users have the ability to mark tasks as completed. The application displays the task list and then prompts the user to select a task index, and upon confirmation, the specified task is marked as completed.

# **4. Delete Task**

This feature allows users to remove unwanted tasks from the manager. Similar to marking as completed, the application prompts the user to select a task index for deletion.

# **5. Sort Tasks by Due Date**

The Task Manager provides functionality to sort tasks based on their due dates. Incomplete tasks are sorted in ascending order of due dates, ensuring a clear view of upcoming deadlines.

# **6. Show Upcoming Tasks**

Users can visualize their upcoming tasks using this feature. The application identifies incomplete tasks with due dates beyond the current date and displays them in a neatly formatted table.

# **7. Data Persistence**

The project incorporates data persistence by saving tasks to a JSON file ('tasks.json'). This ensures that tasks are retained even after closing and reopening the application.

## How to Use

To use the Task Manager, follow these steps:

1.Run the 'project.py' file.
2.Choose from the available options in the menu to perform different operations.
3.Input the required details such as task name, description, due date, and task index when prompted.

## Dependencies

The project relies on the following external libraries:

* 'json': Used for reading and writing tasks to a JSON file.
* 'datetime': Employed for handling date and time information.
* 'PrettyTable': Utilized for creating well-formatted tables for task visualization.

Ensure these libraries are installed before running the project.

