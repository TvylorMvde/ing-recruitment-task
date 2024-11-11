from playwright.sync_api import sync_playwright

from models.modals.cookies import CookiesModal


def before_all(context):
    """Initializes a Playwright browser context and creates a new page
    instance before all tests are run."""
    browser = sync_playwright().start().chromium.launch()
    context.page = browser.new_page()
    return context.page


def before_scenario(context, scenario):
    """Creates a CookiesModal instance and stores it in the context."""
    context.cookies_modal = CookiesModal(context.page)
