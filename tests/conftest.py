import pytest
import logging

from playwright.sync_api import sync_playwright


@pytest.fixture()
def page():
    """Sets up and yields a new browser page."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        context.tracing.start(screenshots=True, snapshots=True)

        yield page

        context.tracing.stop(path="playwright-trace.zip")
        browser.close()


@pytest.fixture()
def remove_cookie_policy_gdpr(page):
    """Removes the 'cookiePolicyGDPR' cookie, if found."""
    cookie_name = "cookiePolicyGDPR"
    logging.info(f"Removing the '{cookie_name}' cookie as a part of the test setup.")
    page.context.clear_cookies(name=cookie_name)
