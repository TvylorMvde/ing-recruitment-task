import logging

from models.modals.cookies import CookiesModal, get_cookie_value


class TestCookies:
    def test_set_analytical_cookies(self, page, remove_policy_gdpr_cookie):
        url = "https://ing.pl"
        logging.info(f"Opening the '{url}' page.")
        page.goto(url)

        logging.info("Clicking the 'Dostosuj' button on the cookie policy modal.")
        cookies_modal = CookiesModal(page)
        cookies_modal.settings.click()

        logging.info(
            "Clicking the 'Cookies analityczne' checkbox on the cookie policy modal."
        )
        cookies_modal.analytical_cookies.click()

        logging.info(
            "Clicking the 'Zaakceptuj wybrane' button on the cookie policy modal."
        )
        cookies_modal.accept_chosen_cookies.click()

        cookie_name = "cookiePolicyGDPR"
        cookie_value = get_cookie_value(page, cookie_name)
        expected_cookie_value = "3"

        logging.info(f"Checking if the '{cookie_name}' cookie has a correct value.")
        assert cookie_value == expected_cookie_value, (
            f"The '{cookie_name}' cookie value does not match the expected one. "
            f"The expected value is '{expected_cookie_value}', but got '{cookie_value}'."
        )
