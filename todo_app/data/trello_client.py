from flask import app, session
from werkzeug.datastructures import Headers
from todo_app.flask_config import Config
from todo_app.data.item import CARD_NAME_KEY, Item, Status
import requests

BASE_URL = 'https://api.trello.com/1'
KEY = Config.TRELLO_DEVELOPER_API_KEY
TOKEN = Config.TRELLO_TOKEN
BOARD_ID = Config.TRELLO_BOARD_ID
NOT_STARTED_LIST_ID = Config.TRELLO_NOT_STARTED_LIST_ID
COMPLETED_LIST_ID = Config.TRELLO_COMPLETED_LIST_ID
BOARD_SPECIFIC_CARDS_URL = f'{BASE_URL}/boards/{BOARD_ID}/cards'
QUERY = {'key': KEY, 'token': TOKEN}
CARDS_URL = f'{BASE_URL}/cards'
LIST_ID_KEY = 'idList'
NAME_KEY = 'name'
HEADERS = {'Accept': 'application/json'}


def get_items():
    cards = requests.get(BOARD_SPECIFIC_CARDS_URL, params=QUERY).json()
    return [Item.create_item_from(card) for card in cards]


def add_item(title):
    return requests.post(CARDS_URL, params={**QUERY, **{LIST_ID_KEY: NOT_STARTED_LIST_ID, NAME_KEY: title}}).status_code == 200


def update_item_whose_id_is(id, status):
    return requests.request(
        "PUT",
        append_id_to_url(CARDS_URL, id),
        headers=HEADERS,
        params={**QUERY, **{LIST_ID_KEY: COMPLETED_LIST_ID if status ==
                            Status.NOT_STARTED.name else NOT_STARTED_LIST_ID}}
    ).status_code == 200


def delete_item_whose_id_is(id):
    return requests.delete(append_id_to_url(CARDS_URL, id), params=QUERY).status_code == 200


def append_id_to_url(url, id):
    return f'{url}/{id}'
