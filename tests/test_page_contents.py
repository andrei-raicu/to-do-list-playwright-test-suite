from pages.to_do_page import ToDoPage

import pytest

from playwright.sync_api import expect, Page


def test_page_title(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # Then the title of the page should be "To Do List"
    expect(to_do_page.title).to_be_visible()
    expect(to_do_page.title).to_have_text("To Do List")


def test_to_do_input_placeholder(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # Then the placeholder of the To Do input should be "What needs to be done?"
    expect(to_do_page.to_do_item_input).to_be_visible()
    expect(to_do_page.to_do_item_input).to_have_attribute(
        "placeholder", "What needs to be done?")


def test_footer_text(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # Then the footer text should be "Double-click to edit a todo"
    expect(to_do_page.footer).to_be_visible()
    expect(to_do_page.footer).to_have_text("Double-click to edit a todo")


def test_filter_texts(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # And I have a to do list item
    to_do_page.create_to_do_items("Test")

    # Then the filter names are "All", "Active" and "Completed"
    expect(to_do_page.all_filter).to_be_visible()
    expect(to_do_page.all_filter).to_have_text("All")

    expect(to_do_page.active_filter).to_be_visible()
    expect(to_do_page.active_filter).to_have_text("Active")

    expect(to_do_page.completed_filter).to_be_visible()
    expect(to_do_page.completed_filter).to_have_text("Completed")
