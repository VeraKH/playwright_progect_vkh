from playwright.async_api import Page, expect
from urllib.parse import urljoin

class ProductPage:
    PRODUCT_DESCRIPTION = '[data-test="product-description"]'
    CART_BUTTON = '[data-test="add-to-cart"]'
    PRODUCT_NAME = '[data-test="product-name"]'
    PRODUCT_URL_BASE = 'https://practicesoftwaretesting.com/product/'

    def __init__(self, page: Page):
        self.page = page

    async def open_product_page(self, product_url_id=None):
        url_id = product_url_id
        full_url = urljoin(self.PRODUCT_URL_BASE, url_id)
        await self.page.goto(full_url)

    def product_description_locator(self):
        return self.page.locator(self.PRODUCT_DESCRIPTION)

    def cart_button_locator(self):
        return self.page.locator(self.CART_BUTTON)