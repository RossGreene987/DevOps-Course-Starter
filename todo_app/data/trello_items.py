import os
import requests
from more_itertools import one

from todo_app.data.models import Item, Status


def get_items():
    url = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/lists"

    response = _make_authorised_request(url, cards="open")

    return [
        Item.from_trello_card(card, list_)
        for list_ in response
        for card in list_["cards"]
    ]


def get_sorted_items():
    status_order = [Status.TODO, Status.STARTED, Status.COMPLETED]
    return sorted(get_items(), key=lambda item: status_order.index(item.status))


def add_item(title):
    url = f"https://api.trello.com/1/cards"
    _make_authorised_request(url, "POST", name=title, idList=_get_list_id(Status.TODO))


def move_item(item_id, status):
    url = f"https://api.trello.com/1/cards/{item_id}"
    _make_authorised_request(url, "PUT", idList=_get_list_id(status))


def remove_item(item_id):
    url = f"https://api.trello.com/1/cards/{item_id}"
    _make_authorised_request(url, "DELETE")


def _make_authorised_request(url, method="GET", **extra_params):
    return requests.request(
        method,
        url,
        params=dict(
            {"key": os.getenv("TRELLO_API_KEY"), "token": os.getenv("TRELLO_TOKEN")},
            **extra_params,
        ),
    ).json()


def _get_list_id(status: Status):
    url = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/lists"
    response = _make_authorised_request(url)
    return one([list_["id"] for list_ in response if Status(list_["name"]) == status])
