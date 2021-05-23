from flask import session
import uuid

_DEFAULT_ITEMS = [
    { 'id': 'f8f7144d-3004-4c7a-90ab-09dc7e46ce13', 'title': 'List saved todo items', 'status': 'Completed' },
    { 'id': '662d8071-6571-4a95-b854-ff3ce7f2da48', 'title': 'Allow new items to be added', 'status': 'Completed' }
]

def create_random_uuid():
    return str(uuid.uuid4())

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return sorted(session.get('items', _DEFAULT_ITEMS.copy()), key=lambda k: k['status'], reverse=True)

def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    return next((item for item in get_items() if item['id'] == id), None)

def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    existing_items = get_items()

    item = { 'id': str(uuid.uuid4()), 'title': title, 'status': 'Not Started' }

    existing_items.append(item)

    session['items'] = existing_items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()

    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item


def delete_item_whose_id_is(id):
    """
    Deletes an existing item in the session.

    Args:
        id: The unique identifier of the item to be deleted
    """
    session['items'] = list(filter(lambda item: item['id'] != id, get_items()))

def derive_opposite_status(status):
    return 'Completed' if status != 'Completed' else 'Not Started'
