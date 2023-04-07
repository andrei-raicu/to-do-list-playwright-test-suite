from pages.to_do_page import ToDoPage

import pytest

from playwright.sync_api import expect, Page


ITEMS = ["Laundry", "Cooking", "Groceries"]


def test_completed_to_dos_should_appear_in_completed_filter(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # And I have 1 to do list item
    to_do_page.create_to_do_items(ITEMS[0])

    # When I mark my to do list item as completed
    to_do_page.mark_to_do_completed_buttons.nth(0).check()

    # Then I expect to do item to be checked
    expect(to_do_page.mark_to_do_completed_buttons.nth(0)).to_be_checked()

    # And I expect to see it in All to dos
    expect(to_do_page.to_do_list_items.nth(0)).to_have_text(ITEMS[0])

    # And I expect NOT to see it in active to dos
    to_do_page.active_filter.click()
    assert to_do_page.to_do_list_items.all_inner_texts() == []

    # And I expect to see it the Completed to dos
    to_do_page.completed_filter.click()
    expect(to_do_page.to_do_list_items.nth(0)).to_have_text(ITEMS[0])
    expect(to_do_page.mark_to_do_completed_buttons.nth(0)).to_be_checked()


def test_mark_all_as_completed(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # And I have multiple to do list items
    to_do_page.create_to_do_items(*ITEMS)

    # When I click on the mark all as completed button
    to_do_page.mark_all_completed_button.click()

    # Then I expect all to do items to be checked
    for index in range(len(ITEMS)):
        expect(to_do_page.mark_to_do_completed_buttons.nth(index)).to_be_checked()
        expect(to_do_page.to_do_list_items.nth(
            index)).to_have_text(ITEMS[index])

    # And I expect NOT to see them in active to dos
    to_do_page.active_filter.click()
    assert to_do_page.to_do_list_items.all_inner_texts() == []

    # And I expect to see them in the Completed to dos
    to_do_page.completed_filter.click()
    assert to_do_page.to_do_list_items.all_inner_texts() == ITEMS


FILTERS = ["all", "completed"]


@pytest.mark.parametrize("filter", FILTERS)
def test_clear_button_should_remove_completed_items(page: Page, to_do_page: ToDoPage, filter: str) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # And I have multiple completed to do list items
    to_do_page.create_to_do_items(*ITEMS)
    if filter == "completed":
        to_do_page.completed_filter.click()
    to_do_page.mark_all_completed_button.click()

    # When I click on the Clear button
    to_do_page.clear_button.click()

    # Then I expect all completed actions to be cleared
    assert to_do_page.to_do_list_items.all_inner_texts() == []


def test_clicking_clear_on_a_list_having_both_active_and_completed_to_dos_clears_only_completed(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # And I have 1 completed to do list item
    # And I have 1 active to do list item
    to_do_page.create_to_do_items(*ITEMS[:2])
    to_do_page.mark_to_do_completed_buttons.nth(0).click()

    # When I click on Clear button
    to_do_page.clear_button.click()

    # Then I expect Active items to remain in the list
    assert to_do_page.to_do_list_items.all_inner_texts() == ITEMS[1:2]

    # And I expect all completed actions to be cleared
    to_do_page.completed_filter.click()
    assert to_do_page.to_do_list_items.all_inner_texts() == []


def test_mark_as_completed_can_be_done_in_active_filtering(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # And I have a created to do list item
    to_do_page.create_to_do_items(ITEMS[0])

    # And I am on the Active filter
    to_do_page.active_filter.click()

    # When I mark the do list item as completed
    to_do_page.mark_to_do_completed_buttons.nth(0).click()

    # Then the item moves to the completed list
    assert to_do_page.to_do_list_items.all_inner_texts() == []
    to_do_page.completed_filter.click()
    assert to_do_page.to_do_list_items.all_inner_texts() == ITEMS[:1]


def test_unmark_as_completed_can_be_done_in_completed_filtering(page: Page, to_do_page: ToDoPage) -> None:
    # Given I am on the To Do List page
    to_do_page.load()

    # And I have a created to do list item marked as completed
    to_do_page.create_to_do_items(ITEMS[0])
    to_do_page.mark_to_do_completed_buttons.nth(0).click()

    # And I am on the Completed filter
    to_do_page.completed_filter.click()

    # When I unmark the to do list item as completed
    to_do_page.mark_to_do_completed_buttons.nth(0).click()

    # Then the items no longer appears in the completed list
    assert to_do_page.to_do_list_items.all_inner_texts() == []

    # And the item appears in the active list
    to_do_page.active_filter.click()
    assert to_do_page.to_do_list_items.all_inner_texts() == ITEMS[:1]

    # And the item appers in the All list
    to_do_page.all_filter.click()
    assert to_do_page.to_do_list_items.all_inner_texts() == ITEMS[:1]
