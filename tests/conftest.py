import os
import pytest
import logging

from logs import configure_logging

from playwright.sync_api import sync_playwright


configure_logging()


@pytest.fixture()
def page():
    """Sets up and yields a new browser page. Additionaly sets up tracking and
    creating test report .zip file at the end of the test run."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()

        yield page

        browser_name = os.getenv("BROWSER_NAME", "chromium")
        context.tracing.stop(
            path=f"playwright-report/playwright-report-{browser_name}.zip"
        )
        browser.close()


@pytest.fixture()
def remove_policy_gdpr_cookie(page):
    """Removes the 'cookiePolicyGDPR' cookie, if found."""
    cookie_name = "cookiePolicyGDPR"
    logging.info(f"Removing the '{cookie_name}' cookie as a part of the test setup.")
    page.context.clear_cookies(name=cookie_name)
