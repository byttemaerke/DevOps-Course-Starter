from enum import Enum
from todo_app.flask_config import Config

CARD_ID_KEY = "id"
CARD_NAME_KEY = "name"
LIST_ID_KEY = "idList"
NOT_STARTED_LIST_ID = Config.TRELLO_NOT_STARTED_LIST_ID
COMPLETED_LIST_ID = Config.TRELLO_COMPLETED_LIST_ID


class Status(Enum):
    NOT_STARTED = 1
    COMPLETED = 2


class Item:

    @classmethod
    def create_item_from(cls, card):
        return cls(
            card[CARD_ID_KEY],
            card[CARD_NAME_KEY],
            Status.NOT_STARTED.name if card[LIST_ID_KEY] == NOT_STARTED_LIST_ID else Status.COMPLETED.name
        )

    def __init__(self, id, title, status=Status.NOT_STARTED.name):
        self.id = id
        self.title = title
        self.status = status

    def update_status(self):
        if self.status is Status.NOT_STARTED.name:
            self.status = Status.COMPLETED.name
        else:
            self.status = Status.NOT_STARTED.name
