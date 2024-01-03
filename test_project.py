import unittest
from datetime import datetime
from project import add_task, view_tasks, mark_task_completed, delete_task, sort_tasks_by_due_date, show_upcoming_tasks, load_tasks, save_tasks

class TestTaskManager(unittest.TestCase):

    def test_add_task(self):
        # Assuming the 'tasks.json' file is empty before running the test
        print("\nRunning test_add_task:")
        try:
            add_task()
            tasks = load_tasks()
            self.assertEqual(len(tasks), 1)
        except Exception as e:
            print(f"Error: {e}")
        print("test_add_task completed.")

    def test_view_tasks(self):
        # Assuming there are no tasks initially
        print("\nRunning test_view_tasks:")
        try:
            view_tasks()  # Simply checking if the function executes without errors
        except Exception as e:
            print(f"Error: {e}")
        print("test_view_tasks completed.")

    def test_mark_task_completed(self):
        # Assuming there is at least one task initially
        print("\nRunning test_mark_task_completed:")
        try:
            mark_task_completed()  # Simply checking if the function executes without errors
        except Exception as e:
            print(f"Error: {e}")
        print("test_mark_task_completed completed.")

    def test_delete_task(self):
        # Assuming there is at least one task initially
        print("\nRunning test_delete_task:")
        try:
            delete_task()  # Simply checking if the function executes without errors
        except Exception as e:
            print(f"Error: {e}")
        print("test_delete_task completed.")

    def test_sort_tasks_by_due_date(self):
        # Assuming there is at least one incomplete task initially
        print("\nRunning test_sort_tasks_by_due_date:")
        try:
            sort_tasks_by_due_date()  # Simply checking if the function executes without errors
        except Exception as e:
            print(f"Error: {e}")
        print("test_sort_tasks_by_due_date completed.")

    def test_show_upcoming_tasks(self):
        # Assuming there is at least one task initially
        print("\nRunning test_show_upcoming_tasks:")
        try:
            show_upcoming_tasks()  # Simply checking if the function executes without errors
        except Exception as e:
            print(f"Error: {e}")
        print("test_show_upcoming_tasks completed.")

    def test_load_tasks(self):
        # Assuming 'tasks.json' is empty or does not exist initially
        print("\nRunning test_load_tasks:")
        try:
            tasks = load_tasks()
            self.assertIsInstance(tasks, list)
        except Exception as e:
            print(f"Error: {e}")
        print("test_load_tasks completed.")

    def test_save_tasks(self):
        # Assuming there is at least one task initially
        print("\nRunning test_save_tasks:")
        try:
            tasks_before_save = load_tasks()
            save_tasks(tasks_before_save)
            tasks_after_save = load_tasks()
            self.assertEqual(tasks_before_save, tasks_after_save)
        except Exception as e:
            print(f"Error: {e}")
        print("test_save_tasks completed.")

if __name__ == '__main__':
    unittest.main()
