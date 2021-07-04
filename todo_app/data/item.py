from enum import Enum
from todo_app.flask_config import Config

CARD_ID_KEY = "id"
CARD_NAME_KEY = "name"
LIST_ID_KEY = "idList"
TODO_LIST_ID = Config.TRELLO_TODO_LIST_ID
DOING_LIST_ID = Config.TRELLO_DOING_LIST_ID
DONE_LIST_ID = Config.TRELLO_DONE_LIST_ID

class Status(Enum):
    TODO = 1
    DOING = 2
    DONE = 3

class Item:
    @classmethod
    def create_item_from(cls, card):
        card_list_id_key = card[LIST_ID_KEY]

        if card_list_id_key == TODO_LIST_ID:
            status = Status.TODO.name
        elif card_list_id_key == DOING_LIST_ID:
            status = Status.DOING.name
        else:
            status = Status.DONE.name

        return cls(card[CARD_ID_KEY], card[CARD_NAME_KEY], status)

    def __init__(self, id, title, status=Status.TODO.name):
        self.id = id
        self.title = title
        self.status = status