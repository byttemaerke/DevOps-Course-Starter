from unittest.mock import patch, Mock
from flask import app

import pytest
from dotenv import load_dotenv, find_dotenv

from todo_app.app import create_app

TRELLO_BOARD_ID = 'trello-board-id'
TODO_LIST_ID = '2'
DOING_LIST_ID = '3'
DONE_LIST_ID = '4'
DONE_LIST_ID = '5'
TODO_TASK_ID = '6'
DOING_TASK_ID = '7'
DONE_TASK_ID = '8'
TRELLO_LIST_RESPONSE_JSON_STUB = [
    {
        'id': TODO_LIST_ID,
        'name': 'To Do',
        'closed': False,
        'pos': 12345,
        'softLimit': None,
        'idBoard': TRELLO_BOARD_ID,
        'subscribed': False,
        'cards':
        [
            {
                'id': TODO_TASK_ID,
                'checkItemStates': None,
                'closed': False,
                'dateLastActivity': '2021-07-29T14:51:05.509Z',
                'desc': '',
                'descData': None,
                'dueReminder': None,
                'idBoard': TRELLO_BOARD_ID,
                'idList': TODO_LIST_ID,
                'idMembersVoted': [],
                'idShort': TODO_TASK_ID[0:2],
                'idAttachmentCover': None,
                'idLabels': [],
                'manualCoverAttachment': False,
                'name': 'Test',
                'pos': 12345,
                'shortLink': 'u39wgurO',
                'isTemplate': False,
                'cardRole': None,
                'badges':{
                    'attachmentsByType': {
                        'trello': {
                            'board': 0,
                            'card': 0
                        }
                    },
                    'location': False,
                    'votes': 0,
                    'viewingMemberVoted': False,
                    'subscribed': False,
                    'fogbugz': '',
                    'checkItems': 0,
                    'checkItemsChecked': 0,
                    'checkItemsEarliestDue': None,
                    'comments': 0,
                    'attachments': 0,
                    'description': False,
                    'due': None,
                    'dueComplete': False,
                    'start': None
                }
            }
        ]
    },
    {
        'id': DOING_LIST_ID,
        'name': 'Doing',
        'cards':
        [
            {
                'id': DOING_TASK_ID,
                'checkItemStates': None,
                'closed': False,
                'dateLastActivity': '2021-07-29T14:51:05.509Z',
                'desc': '',
                'descData': None,
                'dueReminder': None,
                'idBoard': TRELLO_BOARD_ID,
                'idList': DOING_LIST_ID,
                'idMembersVoted': [],
                'idShort': DOING_TASK_ID[0:2],
                'idAttachmentCover': None,
                'idLabels': [],
                'manualCoverAttachment': False,
                'name': 'Test',
                'pos': 12345,
                'shortLink': 'u39wgurO',
                'isTemplate': False,
                'cardRole': None,
                'badges':{
                    'attachmentsByType': {
                        'trello': {
                            'board': 0,
                            'card': 0
                        }
                    },
                    'location': False,
                    'votes': 0,
                    'viewingMemberVoted': False,
                    'subscribed': False,
                    'fogbugz': '',
                    'checkItems': 0,
                    'checkItemsChecked': 0,
                    'checkItemsEarliestDue': None,
                    'comments': 0,
                    'attachments': 0,
                    'description': False,
                    'due': None,
                    'dueComplete': False,
                    'start': None
                }
            }
        ]
    },
    {
        'id': DONE_LIST_ID,
        'name': 'Done',
        'cards':
        [
            {
                'id': DONE_TASK_ID,
                'checkItemStates': None,
                'closed': False,
                'dateLastActivity': '2021-07-29T14:51:05.509Z',
                'desc': '',
                'descData': None,
                'dueReminder': None,
                'idBoard': TRELLO_BOARD_ID,
                'idList': DONE_LIST_ID,
                'idMembersVoted': [],
                'idShort': DONE_TASK_ID[0:2],
                'idAttachmentCover': None,
                'idLabels': [],
                'manualCoverAttachment': False,
                'name': 'Test',
                'pos': 12345,
                'shortLink': 'u39wgurO',
                'isTemplate': False,
                'cardRole': None,
                'badges':{
                    'attachmentsByType': {
                        'trello': {
                            'board': 0,
                            'card': 0
                        }
                    },
                    'location': False,
                    'votes': 0,
                    'viewingMemberVoted': False,
                    'subscribed': False,
                    'fogbugz': '',
                    'checkItems': 0,
                    'checkItemsChecked': 0,
                    'checkItemsEarliestDue': None,
                    'comments': 0,
                    'attachments': 0,
                    'description': False,
                    'due': None,
                    'dueComplete': False,
                    'start': None
                }
            }
        ]
    }
]

@pytest.fixture
def client():
    # Use our test integrastion config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

@patch('requests.get')
def test_index_page(mock_get_requests, client):
    # Replace call to requests.get(url) with our own function
    mock_get_requests.side_effect = mock_get_lists

    response = client.get('/')

    response_html = response.data.decode()
    assert 'To-Do' in response_html
    assert 'Doing' in response_html
    assert 'Done' in response_html

def mock_get_lists(url, params):
    if url == f'https://api.trello.com/1/boards/{TRELLO_BOARD_ID}/lists':
        response = Mock()
        response.json.return_value = TRELLO_LIST_RESPONSE_JSON_STUB
        return response

    return None
