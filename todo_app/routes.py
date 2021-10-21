from flask import render_template, request, redirect, url_for, Blueprint

from todo_app.data import trello_tasks as trello
from todo_app.view_model import ViewModel

todo = Blueprint('todo', __name__)

@todo.route('/')
def index():
    tasks = trello.get_tasks()
    return render_template('index.html', model=ViewModel(tasks))

@todo.route('/tasks/new', methods=['POST'])
def add_task():
    task = request.form['task']
    trello.add_task(task)
    return redirect(url_for('todo.index'))

@todo.route('/tasks/<task_id>/do')
def do_task(task_id):
    trello.do_task(task_id)
    return redirect(url_for('todo.index'))

@todo.route('/tasks/<task_id>/complete')
def complete_task(task_id):
    trello.complete_task(task_id)
    return redirect(url_for('todo.index'))

@todo.route('/tasks/<task_id>/uncomplete')
def uncomplete_task(task_id):
    trello.uncomplete_task(task_id)
    return redirect(url_for('todo.index'))

@todo.route('/tasks/<task_id>')
def delete_task(task_id):
    trello.delete_task(task_id)
    return redirect(url_for('todo.index'))
