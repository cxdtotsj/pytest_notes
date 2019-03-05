import pytest
import tasks
from tasks import Task

def test_add_returns_valid_id(tasks_db):
    """taska.add(<valid task>) should return an integer."""

    # GIVEN an intialized tasks db
    # WHEN a new task is added
    # THEN retruned task_id is of type int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


def test_add_increases_count(do_with_3_tasks):
    """Test tasks.add() affect on tasks.count()."""

    # GIVEN a db with 3 tasks
    # WHEN another task is added
    tasks.add(Task('throw a party'))
    # Then the count increase by 1
    assert tasks.count() == 4