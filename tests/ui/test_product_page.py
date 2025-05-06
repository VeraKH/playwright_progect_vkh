import pytest
from playwright.async_api import expect, Page
from pages.product.product_page import ProductPage
from pages.catalog.product_grid_page import ProductGrid
from pages.main_menu_page import MainMenu
from pages.cart_page import Cart
from pages.auth_page import AuthPage
from data.auth_test_data import (
    valid_user
)

class TestProductPage:

    @pytest.mark.asyncio
    async def test_cart_counter_changes_after_product_is_added(self, main_page):

        product_page = ProductPage(main_page)
        product_grid = ProductGrid(main_page)
        main_menu = MainMenu(main_page)
        cart_page = Cart(main_page)
        auth_page = AuthPage(main_page)

        await product_grid.click_product_by_name("Combination Pliers")
        await product_page.cart_button_locator().click()
        await expect(main_menu.cart_counter_locator()).to_have_text("1")
        await main_menu.click_cart_button()
        await expect(cart_page.proceed_button_locator()).to_be_visible()

        await cart_page.proceed_button_locator().click()
        await auth_page.login(email=valid_user["email"], password=valid_user["password"])







