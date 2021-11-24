from enum import Enum


class Item:
    def __init__(self, id_, title, status):
        self.id = id_
        self.title = title
        self.status = Status(status)

    @classmethod
    def from_trello_card(cls, card, list_):
        return cls(id_=card["id"], title=card["name"], status=list_["name"])

    def __str__(self):
        return f"id: {self.id}, name: {self.title}, status: {self.status}, list_id: {self.list_id}"


class Status(Enum):
    TODO = "To Do"
    STARTED = "Doing"
    COMPLETED = "Done"
