from enum import Enum
from typing import List


class Status(Enum):
    TODO = "To Do"
    STARTED = "Doing"
    COMPLETED = "Done"


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


class ViewModel:
    def __init__(self, items: List[Item]):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def to_do_items(self):
        return self.items_with_status(Status.TODO)

    @property
    def doing_items(self):
        return self.items_with_status(Status.STARTED)

    @property
    def done_items(self):
        return self.items_with_status(Status.COMPLETED)

    def items_with_status(self, status: Status):
        return [item for item in self.items if item.status == status]

    @property
    def should_show_all_done_items(self):
        return len(self.done_items) > 5
