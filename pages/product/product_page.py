from playwright.async_api import Page, expect
from pages.base_page import BasePage

class ProductPage:
    PRODUCT_DESCRIPTION = '[data-test="product-description"]'
    CART_BUTTON = '[data-test="add-to-cart"]'
    PRODUCT_NAME = '[data-test="product-name"]'

    def __init__(self, page: Page):
        self.page = page
        self.base = BasePage(page)

    def product_description_locator(self):
        return self.page.locator(self.PRODUCT_DESCRIPTION)

    def click_button_by_locator(self, locator: str):
        return self.page.locator(locator).click()