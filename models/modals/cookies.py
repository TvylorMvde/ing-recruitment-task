from playwright.sync_api import Page

from typing import Optional

from models.base.clickables import Checkbox, Clickable
from models.base.page import PageElement


def get_cookie_value(page: Page, cookie_name: str) -> Optional[str]:
    """Retrieves the value of the particular cookie by the given name.

    :param page: the Page object
    :param cookie_name: the name of the cookie
    :returns: the value of the cookie or None if the cookie was not found
    """
    cookies = page.context.cookies()
    for cookie in cookies:
        if cookie["name"] == cookie_name:
            return cookie["value"]


class CookiesModal(PageElement):
    """Cookie policy modal with buttons and checkboxes, allowing user to accept
    or decline the particular cookies.
    """

    def __init__(self, page: Page):
        super().__init__(page, "//*[@id='cpm-wrapper']")

        # Buttons
        self.settings = Clickable(page, f"{self.locator}//button[text()='Dostosuj']")
        self.accept_chosen_cookies = Clickable(
            page, f"{self.locator}//button[text()='Zaakceptuj wybrane']"
        )

        # Checkboxes
        self.analytical_cookies = Checkbox(
            page,
            f"{self.locator}//label[@for='CpmAnalyticalOption']",
        )
