from playwright.sync_api import Page, Locator


class PageElement:
    """Base class for page elements."""

    def __init__(self, page: Page, locator: str):
        self._page = page
        self._locator = locator

    @property
    def page(self) -> Page:
        return self._page

    @property
    def locator(self) -> str:
        return self._locator

    @property
    def webelement(self) -> Locator:
        """The object representing the actual page element as found using the provided
        locator.
        """
        return self.page.locator(self.locator)

    @property
    def inner_text(self) -> str:
        return self.webelement.inner_text()
