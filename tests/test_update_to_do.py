from pages.to_do_page import ToDoPage

import pytest

from playwright.sync_api import expect, Page


def test_update_a_to_do_item(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List Page
    to_do_page.load()

    # And I have 1 to do list item
    to_do_page.create_to_do_items("Clean huset")

    # When I edit my to do list item
    to_do_page.update_to_do_items((0, "Clean house"))

    # Then I expect to see the updated item
    expect(to_do_page.to_do_list_items.nth(0)).to_have_text("Clean house")


def test_update_an_active_to_do_item(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # And I have 1 to do list item
    to_do_page.create_to_do_items("Clean huset")

    # And I have selected the Active filter
    to_do_page.active_filter.click()

    # When I edit my to do list item
    to_do_page.update_to_do_items((0, "Clean house"))

    # Then I expect to see the updated item
    expect(to_do_page.to_do_list_items.nth(0)).to_have_text("Clean house")


def test_update_a_completed_to_do_item(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # And I have 1 completed to do list item
    to_do_page.create_to_do_items("Clean huset")
    to_do_page.mark_to_do_completed_buttons.nth(0).check()

    # And I have selected the Completed filter
    to_do_page.completed_filter.click()

    # When I edit my completed item
    to_do_page.update_to_do_items((0, "Clean house"))

    # Then I expect to see the updated item
    expect(to_do_page.to_do_list_items.nth(0)).to_have_text("Clean house")
