import pytest
import logging

from playwright.sync_api import sync_playwright


logger = logging.getLogger(__name__)


@pytest.fixture()
def page():
    """Sets up and yields a new browser page."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture()
def remove_cookie_policy_gdpr(page):
    """Removes the 'cookiePolicyGDPR' cookie, if found."""
    cookie_name = "cookiePolicyGDPR"
    logger.info(f"Removing the '{cookie_name}' cookie as a part of the test setup.")
    page.context.clear_cookies(name=cookie_name)
