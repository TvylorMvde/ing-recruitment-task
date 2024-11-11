import logging

from typing import Optional

from models.modals.cookies import CookiesModal

from playwright.sync_api import Page


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
    def test_set_analytical_cookies(self, page, remove_policy_gdpr_cookie):
        logging.info("Opening the 'ing.pl' page.")
        page.goto("https://ing.pl")

        logging.info("Clicking the 'Dostosuj' button on the cookie policy modal.")
        cookies_modal = CookiesModal(page)
        cookies_modal.settings.click()

        logging.info(
            "Clicking the 'Cookies analityczne' checkbox on the cookie policy modal."
        )
        cookies_modal.analitycal_cookies.click()

        logging.info(
            "Clicking the 'Zaakceptuj wybrane' button on the cookie policy modal."
        )
        cookies_modal.accept_chosen_cookies.click()

        cookie_name = "cookiePolicyGDPR"
        cookie_value = get_cookie_value(page, cookie_name)
        expected_value = "3"

        logging.info(f"Checking if the '{cookie_name}' cookie has a correct value.")
        assert cookie_value == expected_value, (
            f"The '{cookie_name}' cookie value does not match the expected one. "
            f"The expected value is '{expected_value}', but got '{cookie_value}'."
        )
