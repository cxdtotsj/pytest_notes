import pytest
import tasks
from tasks import Task


tasks_to_try = (
    Task('sleep', done=True),
    Task('wake', 'brian'),
    Task('breathe', 'BRIAN', True),
    Task('exercise', 'BrIaN', False)
)

task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done) for t in tasks_to_try]

def equivalent(t1, t2):
    """Check two tasks for equivalence."""

    # Compare everything but the id field
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))

# 对 fixture 进行参数化
@pytest.fixture(params=tasks_to_try,ids=task_ids)
def a_task(request):
    """Using no ids."""

    return request.param

def test_add_a(tasks_db, a_task):
    """Using a_task fixture (no ids)."""

    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, a_task)


# 对 fixture 进行参数化, 增加 ids 标识
@pytest.fixture(params=tasks_to_try,ids=task_ids)
def b_task(request):
    """Using no ids."""

    return request.param

def test_add_b(tasks_db, b_task):
    """Using a_task fixture (no ids)."""

    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)


# ids 参数可以被指定为一个函数，供pytest生成task标识
def id_func(fixture_value):
    t = fixture_value
    return 'Task({},{},{})'.format(t.summary, t.owner, t.done)

@pytest.fixture(params=tasks_to_try,ids=id_func)
def c_task(request):
    """Using no ids."""

    return request.param

def test_add_c(tasks_db, c_task):
    """Using a_task fixture (no ids)."""

    task_id = tasks.add(c_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, c_task)