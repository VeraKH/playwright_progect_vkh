import pytest
from playwright.async_api import expect, Page
from pages.catalog.product_grid_page import CatalogPage
from pages.product.product_page import ProductPage
from pages.main_menu_page import MainMenu
from pages.auth_page import AuthPage
from data.auth_test_data import valid_users


class TestCataProductNavigation:

    @pytest.mark.asyncio
    async def test_click_on_product_opens_product_page(self, main_page: Page):
        catalog_page = CatalogPage(main_page)
        product_page = ProductPage(main_page)

        await catalog_page.click_product_by_name("Combination Pliers")
        await main_page.wait_for_timeout(2000)

        await expect(product_page.product_description_locator()).to_be_visible()

    @pytest.mark.parametrize("user_data, expected_text", valid_users)
    @pytest.mark.asyncio
    async def test_add_to_card_get_product_in_cart(self, main_page: Page, user_data, expected_text):
        catalog_page = CatalogPage(main_page)
        product_page = ProductPage(main_page)
        main_menu = MainMenu(main_page)
        auth_page = AuthPage(main_page)


        await catalog_page.click_product_by_name("Combination Pliers")
        await product_page.click_button_by_locator(product_page.CART_BUTTON)
        await expect(main_menu.cart_counter_locator()).to_have_text("1")

        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await main_page.goto("https://practicesoftwaretesting.com")
