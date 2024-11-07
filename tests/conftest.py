import pytest

from playwright.sync_api import sync_playwright


@pytest.fixture()
def page():
    """Sets up and yields a new browser page."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture()
def remove_cookie_policy_gdpr(page):
    """Removes the 'cookiePolicyGDPR' cookie, if found."""
    page.context.clear_cookies(name="cookiePolicyGDPR")
