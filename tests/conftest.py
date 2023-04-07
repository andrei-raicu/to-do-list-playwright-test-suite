from playwright.sync_api import Page

import pytest

from pages.to_do_page import ToDoPage


@pytest.fixture
def to_do_page(page: Page) -> ToDoPage:
    return ToDoPage(page)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1400,
            "height": 1080,
        }
    }
