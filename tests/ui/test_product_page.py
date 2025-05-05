import pytest
from playwright.async_api import expect, Page
from pages.product.product_page import ProductPage
from data.product_urls import products

class TestProductPage:

    @pytest.mark.asyncio
    async def test_product_is_added_to_cart(self, page: Page):
        product_page = ProductPage(page)

        await  product_page.open_product_page(products["Combination Pliers"])
        await product_page.cart_button_locator().click()

