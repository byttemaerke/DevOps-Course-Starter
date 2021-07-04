import os


class Config:

    def raise_error_if_omitted(env_vars):
        for env_var in env_vars:
            if not env_var:
                raise ValueError(
                    f"No {env_var} set for Flask application. Did you follow the setup instructions?")

    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TRELLO_DEVELOPER_API_KEY = os.environ.get('TRELLO_DEVELOPER_API_KEY')
    TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
    TRELLO_BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
    TRELLO_TODO_LIST_ID = os.environ.get('TRELLO_TODO_LIST_ID')
    TRELLO_DOING_LIST_ID = os.environ.get('TRELLO_DOING_LIST_ID')
    TRELLO_DONE_LIST_ID = os.environ.get('TRELLO_DONE_LIST_ID')

    raise_error_if_omitted([
        SECRET_KEY,
        TRELLO_DEVELOPER_API_KEY,
        TRELLO_TOKEN,
        TRELLO_BOARD_ID,
        TRELLO_TODO_LIST_ID,
        TRELLO_DOING_LIST_ID,
        TRELLO_DONE_LIST_ID
    ])
