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

@pytest.mark.skip(reason='misunderstood the API')
def test_unique_id():
    """Calling unique twice should return different numbers."""

    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

