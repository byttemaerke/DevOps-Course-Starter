from todo_app.data.task import Task
import requests
from flask import current_app as app

def get_auth_params():
    return { 'key': app.config['TRELLO_API_KEY'], 'token': app.config['TRELLO_TOKEN'] }

def build_url(endpoint):
    return app.config['TRELLO_BASE_URL'] + endpoint

def build_params(params={}):
    full_params = get_auth_params()
    full_params.update(params)
    return full_params

def get_lists():
    """
    Fetches all lists for the default Trello board.

    Returns:
        list: The list of Trello lists.
    """
    params = build_params({ 'cards': 'open' }) # Only return cards that have not been archived
    url = build_url('/boards/%s/lists' % app.config['TRELLO_BOARD_ID'])
    response = requests.get(url, params = params)
    lists = response.json()

    return lists

def get_list(name):
    """
    Fetches the list from Trello with the specified name.

    Returns:
        list: The list and its tasks (cards) or None if no list matches the specified name
    """
    lists = get_lists()
    return next((list for list in lists if list['name'] == name), None)

def get_tasks():
    """
    Fetches all tasks (known as "cards") from Trello.

    Returns:
        list: The list of saved tasks.
    """
    lists = get_lists()

    tasks = []
    for card_list in lists:
        for card in card_list['cards']:
            tasks.append(Task.fromTrelloCard(card, card_list))
    
    return tasks

def add_task(name):
    """
    Adds a new task with the specified name as a Trello card.

    Args:
        name (str): THe name of the task.
    
    Returns:
        task: The saved task.
    """
    todo_list = get_list('To Do')

    params = build_params({ 'name': name, 'idList': todo_list['id']})
    url = build_url('/cards')

    response = requests.post(url, params = params)
    card = response.json()

    return Task.fromTrelloCard(card, todo_list)

def do_task(id):
    """
    Moves the task with the specified ID to the "Doing" list in Trello.

    Args:
        id (str): The ID of the task.

    Returns:
        task: The saved task or None if no tasks match the specified ID.
    """
    doing_list = get_list('Doing')
    card = move_card_to_list(id, doing_list)

    return Task.fromTrelloCard(card, doing_list)

def complete_task(id):
    """
    Moves the task with the specified ID to the "Done" list in Trello.
    
    Args:
        id (str): The ID of the task.
    
    Returns:
        task: The saved task or None if no tasks match the specified ID.
    """
    done_list = get_list('Done')
    card = move_card_to_list(id, done_list)

    return Task.fromTrelloCard(card, done_list)

def uncomplete_task(id):
    """
    Moves the task with the specified ID to the "To-Do" list in Trello.
    
    Args:
        id (str): The ID of the task.
    
    Returns:
        task: The saved task or None if no tasks match the specified ID.
    """
    todo_list = get_list('To Do')
    card = move_card_to_list(id, todo_list)

    return Task.fromTrelloCard(card, todo_list)

def delete_task(id):
    """
    Deletes the task with the specified ID from Trello.
    
    Args:
        id (str): The ID of the task.
    
    Returns:
        None 
    """
    url = build_url('/cards/%s' % id)
    requests.delete(url, params = build_params())

def move_card_to_list(card_id, list):
    params = build_params({ 'idList': list['id']})
    url = build_url('/cards/%s' % card_id)

    response = requests.put(url, params = params)
    card = response.json()

    return card