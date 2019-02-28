import pytest
import tasks

def test_add_raises():
    """add() should raise an exception with wrong type param"""

    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')

def test_start_tasks_db_raise():
    """make sure unsupported db raise an exception."""

    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'" 