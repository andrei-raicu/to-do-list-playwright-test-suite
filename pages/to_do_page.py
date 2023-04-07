from playwright.sync_api import Page

from typing import Tuple

import platform


class ToDoPage:

    TITLE = ".header > h1"
    TO_DO_ITEM_INPUT = "input[class*=new-todo]"
    FOOTER = "footer > p"
    TO_DO_LIST_ITEMS = "ul[class=todo-list] > li"
    TO_DO_COUNTER = ".todo-count"
    ALL_FILTER = "a[href=\"#/\"]"
    ACTIVE_FILTER = "a[href=\"#/active\"]"
    COMPLETED_FILTER = "a[href=\"#/completed\"]"
    CLEAR_BUTTON = "button[class=clear-completed]"
    MARK_TO_DO_COMPLETED_BUTTONS = ".todo-list input[type=checkbox]"
    REMOVE_TO_DO_ITEM_BUTTONS = "button[class=destroy]"
    MARK_ALL_COMPLETED_BUTTON = "label[for=toggle-all]"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.locator(self.TITLE)
        self.to_do_item_input = page.locator(self.TO_DO_ITEM_INPUT)
        self.footer = page.locator(self.FOOTER)
        self.to_do_list_items = page.locator(self.TO_DO_LIST_ITEMS)
        self.to_do_counter = page.locator(self.TO_DO_COUNTER)
        self.all_filter = page.locator(self.ALL_FILTER)
        self.active_filter = page.locator(self.ACTIVE_FILTER)
        self.completed_filter = page.locator(self.COMPLETED_FILTER)
        self.clear_button = page.locator(self.CLEAR_BUTTON)
        self.mark_to_do_completed_buttons = page.locator(
            self.MARK_TO_DO_COMPLETED_BUTTONS)
        self.remove_to_do_item_buttons = page.locator(
            self.REMOVE_TO_DO_ITEM_BUTTONS)
        self.mark_all_completed_button = page.locator(
            self.MARK_ALL_COMPLETED_BUTTON)

    @property
    def url(self) -> str:
        return "https://todolist.james.am/"

    def load(self) -> None:
        self.page.goto(self.url)

    def create_to_do_items(self, *to_do_items: str) -> None:
        for item in to_do_items:
            self.to_do_item_input.fill(item)
            self.page.keyboard.press("Enter")

    def update_to_do_items(self, *to_do_items: Tuple[int, str]) -> None:
        for index, updated_value in to_do_items:
            self.to_do_list_items.nth(index).dblclick()

            select_all_combo = "Meta+A" if platform.system() == "Darwin" else "Control+A"

            self.to_do_list_items.nth(index).press(select_all_combo)
            self.to_do_list_items.nth(index).press("Backspace")

            for ch in updated_value:
                self.to_do_list_items.nth(index).press(ch)
            self.to_do_list_items.nth(index).press("Enter")

    def delete_to_do_items(self, *to_do_indexes: int) -> None:
        for index in to_do_indexes:
            self.to_do_list_items.nth(index).hover()
            self.remove_to_do_item_buttons.nth(index).click()
