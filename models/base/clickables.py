from playwright.sync_api import Page

from models.base.page import PageElement


class Clickable(PageElement):
    """Base class for clickable elements e.g. buttons, checkboxes."""

    def __init__(self, page: Page, locator: str):
        super().__init__(page, locator)

    def click(self):
        self.webelement.click()


class Checkbox(Clickable):
    """Base class for checkboxes."""

    def __init__(self, page: Page, locator: str):
        super().__init__(page, locator)
