import os
import pytest
import logging

from logs import configure_logging

from playwright.sync_api import sync_playwright


configure_logging()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        choices=["chromium", "firefox"],
        help="Specify which browser to use (chromium or firefox)",
    )


@pytest.fixture()
def page(request):
    """Sets up and yields a new browser page. Additionaly sets up tracking and
    creating test report .zip file at the end of the test run."""
    browser_name = request.config.getoption("--browser")
    with sync_playwright() as playwright:
        browser = getattr(playwright, browser_name).launch()
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()

        yield page

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
