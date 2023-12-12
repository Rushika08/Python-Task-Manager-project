import pytest
from project import add_task, view_tasks, mark_task_completed, load_tasks, save_tasks
from datetime import datetime, timedelta

@pytest.fixture
def sample_tasks():
    return [
        {"name": "Task 1", "description": "Description 1", "due_date": "2023-01-01", "completed": False},
        {"name": "Task 2", "description": "Description 2", "due_date": "2023-02-01", "completed": False},
        {"name": "Task 3", "description": "Description 3", "due_date": "2023-03-01", "completed": True},
    ]

def test_add_task(sample_tasks):
    tasks_before = sample_tasks.copy()
    add_task()
    tasks_after = load_tasks()
    assert len(tasks_after) == len(tasks_before) + 1

def test_view_tasks(capfd, sample_tasks):
    tasks = sample_tasks.copy()
    save_tasks(tasks)
    
    view_tasks()
    
    captured = capfd.readouterr()
    for task in tasks:
        assert task["name"] in captured.out

def test_mark_task_completed(sample_tasks):
    tasks = sample_tasks.copy()
    save_tasks(tasks)
    
    mark_task_completed()
    
    tasks_after = load_tasks()
    assert any(task["completed"] for task in tasks_after)
