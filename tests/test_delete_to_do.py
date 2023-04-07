from pages.to_do_page import ToDoPage

import pytest

from playwright.sync_api import expect, Page


ITEMS = ["Clean house", "Do groceries"]
FILTERS = ["all", "active", "completed"]


@pytest.mark.parametrize("filter", FILTERS)
def test_to_do_items_can_be_deleted_from_any_filter(page: Page, to_do_page: ToDoPage, filter: str) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # And I have 2 to do list items
    to_do_page.create_to_do_items(*ITEMS)
    if filter == "completed":
        to_do_page.mark_all_completed_button.click()

    # And I select a given filter
    if filter == "active":
        to_do_page.active_filter.click()
    elif filter == "completed":
        to_do_page.completed_filter.click()

    # When I delete a to do list item
    to_do_page.delete_to_do_items(0)

    # Then the list updates accordingly
    assert to_do_page.to_do_list_items.all_inner_texts() == ITEMS[1:2]
