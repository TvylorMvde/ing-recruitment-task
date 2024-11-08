from playwright.sync_api import Page

from models.base.clickables import Checkbox, Clickable
from models.base.page import PageElement


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
        self.analitycal_cookies = Checkbox(
            page,
            f"{self.locator}//label[@for='CpmAnalyticalOption']",
        )
