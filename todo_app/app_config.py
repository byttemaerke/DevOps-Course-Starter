import os

class Config:
    def __init__(self):
        self.TRELLO_BASE_URL = 'https://api.trello.com/1'
        self.TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
        self.TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
        self.TRELLO_BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
        self.raise_error_if_omitted([
            self.TRELLO_BASE_URL,
            self.TRELLO_API_KEY,
            self.TRELLO_TOKEN,
            self.TRELLO_BOARD_ID]
        )

    def raise_error_if_omitted(self, env_vars):
        for env_var in env_vars:
            if not env_var:
                raise ValueError(
                    f"An environment variable has not been set for this Flask application. Did you follow the setup instructions?")
