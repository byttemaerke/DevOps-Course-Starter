import pytest

from datetime import datetime

from freezegun import freeze_time

from todo_app.data.trello_tasks import Task
from todo_app.view_model import ViewModel

def test_getters_return_empty_lists_if_no_tasks_exist():
    tasks = []
    view_model = ViewModel(tasks)

    assert len(view_model.to_do_tasks) == 0
    assert len(view_model.doing_tasks) == 0
    assert len(view_model.done_tasks) == 0

def test_getters_return_corresponding_lists_if_tasks_exist():
    swim_task = Task(1, 'Swim', datetime.now(), 'Done')
    cycle_task = Task(2, 'Cycle', datetime.now(), 'Doing')
    run_task = Task(3, 'Run', datetime.now(), 'To Do')
    tasks = [swim_task, cycle_task, run_task]
    view_model = ViewModel(tasks)

    assert view_model.to_do_tasks == [run_task]
    assert view_model.doing_tasks == [cycle_task]
    assert view_model.done_tasks == [swim_task]

@pytest.fixture
def swim_task():
    return Task(1, 'Swim', datetime(2021, 7, 10, 15, 3, 59), 'Done')

@pytest.fixture
def cycle_task():
    return Task(2, 'Cycle', datetime(2021, 7, 10, 15, 4, 0), 'Done')

@pytest.fixture
def run_task():
    return Task(3, 'Run', datetime(2021, 7, 10, 15, 4, 1), 'Done')

@pytest.fixture
def rest_task():
    return Task(4, 'Rest', datetime(2021, 7, 11, 13, 42, 12), 'Done')

@pytest.fixture
def walk_task():
    return Task(5, 'Walk', datetime(2021, 7, 9, 2, 37, 59), 'Done')

@pytest.fixture
def view_models_with_fewer_than_five_done_tasks(swim_task, cycle_task, run_task, rest_task):
    return [
        ViewModel([swim_task]),
        ViewModel([swim_task, cycle_task]),
        ViewModel([swim_task, cycle_task, run_task]),
        ViewModel([swim_task, cycle_task, run_task, rest_task])
    ]

def test_should_allow_all_done_tasks_if_there_are_fewer_than_five(view_models_with_fewer_than_five_done_tasks):
    assert all(view_model.should_show_all_done_tasks for view_model in view_models_with_fewer_than_five_done_tasks)

@freeze_time("2021-07-10 15:04:00")
def test_should_not_allow_all_done_tasks_if_there_are_five_or_more(swim_task, cycle_task, run_task, rest_task, walk_task):
    view_model_with_five_done_tasks = ViewModel([swim_task, cycle_task, run_task, rest_task, walk_task])

    assert view_model_with_five_done_tasks.should_show_all_done_tasks is False
    assert view_model_with_five_done_tasks.recent_done_tasks == [swim_task, cycle_task, run_task]
    assert view_model_with_five_done_tasks.older_done_tasks == [walk_task]
