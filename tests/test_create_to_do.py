from pages.to_do_page import ToDoPage

import pytest

from playwright.sync_api import expect, Page


ITEMS = ["Clean house", "Do groceries", "Do laundry"]


def test_create_three_to_dos(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # When I add 3 do list items
    to_do_page.create_to_do_items(*ITEMS)

    # Then I expect the to do list items to appear in the list
    assert to_do_page.to_do_list_items.all_inner_texts() == ITEMS


def test_to_do_items_count(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List Page
    to_do_page.load()

    # When I add 2 to do list items
    to_do_page.create_to_do_items(*ITEMS[:2])

    # Then I expect counter to have value 2
    expect(to_do_page.to_do_counter).to_have_text('2 items left')


def test_create_to_do_on_active_filter(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List Page
    to_do_page.load()

    # And I have a to do list item
    to_do_page.create_to_do_items(ITEMS[0])

    # And I am on the active filter
    to_do_page.active_filter.click()

    # When I create a to do list item
    to_do_page.create_to_do_items(ITEMS[1])

    # Then I expect to see it in the active filter
    assert to_do_page.to_do_list_items.all_inner_texts() == ITEMS[:2]

    # And I expect to see it in the All filter
    to_do_page.all_filter.click()
    assert to_do_page.to_do_list_items.all_inner_texts() == ITEMS[:2]


def test_create_to_do_on_completed_filter(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List Page
    to_do_page.load()

    # And I have a to do list item
    to_do_page.create_to_do_items(ITEMS[0])

    # And I am on the Completed filter
    to_do_page.completed_filter.click()

    # When I create a to do list item
    to_do_page.create_to_do_items(ITEMS[1])

    # Then I expect NOT to see it in the Completed filter
    assert to_do_page.to_do_list_items.all_inner_texts() == []

    # And I expect to see it in the All and active filters
    filters = [to_do_page.all_filter, to_do_page.active_filter]
    for filter in filters:
        filter.click()
        assert to_do_page.to_do_list_items.all_inner_texts() == ITEMS[:2]
