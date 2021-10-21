import os
from threading import Thread
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import datetime

from todo_app.app_config import Config
from todo_app.app import create_app

def create_trello_board():
    config = Config()
    response = requests.post(
        url=f'{config.TRELLO_BASE_URL}/boards',
        params={
            'key': config.TRELLO_API_KEY,
            'token': config.TRELLO_TOKEN,
            'name': f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}_Selenium_Test_Board'
        }
    )

    return response.json()['id']

def delete_trello_board(board_id):
    config = Config()
    response = requests.delete(
        url=f'{config.TRELLO_BASE_URL}/boards/{board_id}',
        params={
            'key': config.TRELLO_API_KEY,
            'token': config.TRELLO_TOKEN,
        }
    )

@pytest.fixture(scope='module')
def app_with_temp_board():
    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['TRELLO_BOARD_ID'] = board_id

    # construct the new application
    application = create_app()

    # start the app in its own thread
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)

@pytest.fixture(scope='module')
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome('./chromedriver', options=opts) as driver:
        yield driver

def test_task_journey(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')

    assert driver.title == 'To-Do App'
    
    task_title = 'Selenium Test Task'
    task_input = driver.find_element_by_xpath("//*[@data-test-id='task-input']")

    task_input.send_keys(task_title)
    task_input.send_keys(Keys.RETURN)

    to_do_list = driver.find_element_by_xpath(f"//*[@data-test-id='to-do-list']")
    to_do_tasks = to_do_list.find_elements_by_xpath("//*[@data-test-class='task']")

    assert task_title in to_do_tasks[0].text