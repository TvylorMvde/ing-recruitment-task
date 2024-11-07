import logging

from typing import Optional

from models.modals.cookies import CookiesModal

from playwright.sync_api import Page


logger = logging.getLogger(__name__)


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


class TestCookies:
    def test_set_analytical_cookies(self, page, remove_cookie_policy_gdpr):
        logger.info("Opening the 'ing.pl' page.")
        page.goto("https://ing.pl")

        cookies_modal = CookiesModal(page)
        cookies_modal.webelement.scroll_into_view_if_needed()

        logger.info("Clicking the 'Dostosuj' button.")
        cookies_modal.settings.click()

        logger.info("Checking the 'Cookies analityczne' checkbox.")
        cookies_modal.analitycal_cookies.click()

        logger.info("Clicking the 'Zaakceptuj wybrane' button.")
        cookies_modal.accept_chosen_cookies.click()

        cookie_name = "cookiePolicyGDPR"
        logger.info(f"Getting the value of the '{cookie_name}' cookie.")
        cookie_value = get_cookie_value(page, cookie_name)

        logger.info(f"The retrieved '{cookie_name}' cookie value: {cookie_value}.")

        logger.info(f"Checking if the '{cookie_name}' cookie has a correct value.")
        expected_value = "3"
        assert cookie_value == expected_value, (
            f"The '{cookie_name}' cookie value does not match the expected one. "
            f"The expected value is '{expected_value}', but got '{cookie_value}'."
        )
