from flask import session

_DEFAULT_ITEMS = [
    {"id": 1, "status": "Not Started", "title": "List saved todo items"},
    {"id": 2, "status": "Not Started", "title": "Allow new items to be added"},
]


def get_items():
    return session.get("items", _DEFAULT_ITEMS.copy())


def get_sorted_items():
    return sorted(get_items(), key=lambda item: item["status"] == "Completed")


def get_item(id):
    items = get_items()
    return next((item for item in items if item["id"] == int(id)), None)


def add_item(title):
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id_ = items[-1]["id"] + 1 if items else 0
    item = {"id": id_, "title": title, "status": "Not Started"}

    # Add the item to the list
    items.append(item)
    session["items"] = items

    return item


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.
    """
    existing_items = get_items()
    updated_items = [
        item if item["id"] == existing_item["id"] else existing_item
        for existing_item in existing_items
    ]

    session["items"] = updated_items

    return item


def remove_item(item_id):
    session["items"] = [item for item in get_items() if item["id"] != item_id]
