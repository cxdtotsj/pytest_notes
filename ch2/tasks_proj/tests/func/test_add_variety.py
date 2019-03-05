import pytest
import tasks
from tasks import Task


def test_add_1():

    task = Task('breathe', 'BRIAN', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


def equivalent(t1, t2):
    """Check two tasks for equivalence."""

    # Compare everything but the id field
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):

    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()

# task 作为引用函数的参数
@pytest.mark.parametrize('task', [
    Task('sleep', done=True),
    Task('wake', 'brian'),
    Task('breathe', 'BRIAN', True),
    Task('exercise', 'BrIaN', False)])
def test_add_2(task):

    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('summary,owner,done',[
    ('sleep',None,False),
    ('wake','brian',False),
    ('breathe','BRIAN', True),
    ('eat eggs','BrIaN', False)
])
def test_add_3(summary,owner,done):
    task = Task(summary,owner,done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


# 代码看起来比较美观，可读性较差
tasks_to_try = (
    Task('sleep', done=True),
    Task('wake', 'brian'),
    Task('breathe', 'BRIAN', True),
    Task('exercise', 'BrIaN', False)
)
@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):

    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert  equivalent(t_from_db, task)


# ids 参数可为用例生成编号
task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done) for t in tasks_to_try]
@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    """增加 ids."""

    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


# 给类传递 parametrize() 参数
@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd:

    def test_equivalent(self,task):

        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)
    
    def test_vaild_id(self,task):

        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id