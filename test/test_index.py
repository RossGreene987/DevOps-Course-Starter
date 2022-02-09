import os

import requests


class StubResponse:
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data


def test_index_page(monkeypatch, client):
    def get_lists_stub(method, url, params):
        test_board_id = os.environ.get("TRELLO_BOARD_ID")
        fake_response_data = None

        if url == f"https://api.trello.com/1/boards/{test_board_id}/lists":
            fake_response_data = [
                {
                    "id": "12",
                    "name": "To Do",
                    "cards": [{"id": "456", "name": "Test card"}],
                }
            ]

        return StubResponse(fake_response_data)

    monkeypatch.setattr(requests, "request", get_lists_stub)

    response = client.get("/")

    assert response.status_code == 200
    assert "Test card" in response.data.decode()
