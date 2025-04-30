from playwright.async_api import Page

class AdminPage:

    ADMIN_PAGE_TITLE = '[data-test="page-title"]'

    def __init__(self, page: Page):
        self.page = page

    def admin_title_locator(self):
        return self.page.locator(self.ADMIN_PAGE_TITLE)
