import pytest as pytest

from todo_app.data.models import Item, Status, ViewModel


@pytest.fixture
def view_model():
    return ViewModel(
        items=[
            Item(1, "Test app", Status.STARTED),
            Item(2, "Add integration test", Status.TODO),
            Item(3, "Add end to end test", Status.TODO),
        ]
    )


def _assert_item_list_has_ids(item_list, ids_list):
    assert sorted([item.id for item in item_list]) == ids_list


def test_view_model_returns_correct_items(view_model):
    _assert_item_list_has_ids(view_model.items, [1, 2, 3])
    _assert_item_list_has_ids(view_model.to_do_items, [2, 3])
    _assert_item_list_has_ids(view_model.done_items, [])


@pytest.mark.parametrize("number_of_done_items", [5, 6])
def test_view_model_should_show_all_done_items(number_of_done_items):
    view_model = ViewModel(
        items=[Item(i, "Task", Status.COMPLETED) for i in range(number_of_done_items)]
    )
    assert view_model.should_show_all_done_items == (number_of_done_items > 5)
