from playwright.async_api import Page, expect
from pages.base_page import BasePage

class Cart:

    PROCEED_BUTTON = '[data-test="proceed-1"]'

    def __init__(self, page: Page):
        self.page = page


    def proceed_button_locator(self):
        return self.page.locator(self.PROCEED_BUTTON)