from playwright.async_api import Page, expect
from pages.base_page import BasePage

class MainMenu:

    CART_BUTTON = '[data-test="nav-cart"]'
    CART_BUTTON_COUNT = '[data-test="cart-quantity"]'
    SIGN_IN_BUTTON = '[data-test="nav-sign-in"]'
    USER_NAME = '[data-test="nav-menu"]'

    def __init__(self, page: Page):
        self.page = page
        self.base = BasePage(page)

    #Return cart icon counter locator
    def cart_counter_locator(self):
        return self.page.locator(self.CART_BUTTON_COUNT)

    def sign_in_link_exists(self):
        return self.page.locator(self.SIGN_IN_BUTTON)

    def user_name_exists(self):
        return self.page.locator(self.USER_NAME)

    async def click_cart_button(self):
        await self.page.locator(self.CART_BUTTON).click()



