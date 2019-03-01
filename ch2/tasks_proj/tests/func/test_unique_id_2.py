import pytest
import tasks

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""

    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield

    # Teardown: stop db
    tasks.stop_tasks_db()

@pytest.mark.xfail(tasks.__version__<'0.2.0', reason='not supported until version 0.2.0')
def test_unique_id():
    """Calling unique twice should return different numbers."""

    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

@pytest.mark.xfail()
def test_unique_id_is_a_duck():

    uid = tasks.unique_id()
    assert uid == 'a duck'

@pytest.mark.xfail()
def test_unique_id_is_not_a_duck():

    uid = tasks.unique_id()
    assert uid != 'a duck'
    
