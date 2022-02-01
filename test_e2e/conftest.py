import os
from threading import Thread
from selenium import webdriver

import pytest
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver.firefox.options import Options

from todo_app import app


from todo_app.data.trello_items import _make_authorised_request


def create_trello_board():
    load_dotenv(find_dotenv(".env"), override=True)
    board_name = "test-board"
    url = f"https://api.trello.com/1/boards/?name={board_name}"
    request = _make_authorised_request(url, "POST")
    return request["id"]


def delete_trello_board(id):
    url = f"https://api.trello.com/1/boards/{id}"
    _make_authorised_request(url, "DELETE")


@pytest.fixture(scope="module")
def app_with_temp_board():
    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ["TRELLO_BOARD_ID"] = board_id

    application = app.create_app()

    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id)


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.headless = True
    with webdriver.Firefox(options=options) as driver:
        yield driver
