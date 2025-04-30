import pytest
from playwright.async_api import expect, Page
from pages.catalog.product_grid import CatalogPage
from pages.product.product_page import ProductPage
from pages.main_menu import MainMenu
from pages.auth_page import AuthPage
from data.auth_test_data import valid_users


class TestCataProductNavigation:

    @pytest.mark.asyncio
    async def test_click_on_product_opens_product_page(self, page:Page):
        catalog_page = CatalogPage(page)
        product_page = ProductPage(page)

        await catalog_page.click_product_by_name("Combination Pliers")
        await page.wait_for_timeout(2000)

        await expect(product_page.product_description_locator()).to_be_visible()

    @pytest.mark.parametrize("user_data, expected_text", valid_users)
    @pytest.mark.asyncio
    async def test_add_to_card_get_product_in_cart(self, page: Page, user_data, expected_text):
        catalog_page = CatalogPage(page)
        product_page = ProductPage(page)
        main_menu = MainMenu(page)
        auth_page = AuthPage(page)


        await catalog_page.click_product_by_name("Combination Pliers")
        await product_page.click_button_by_locator(product_page.CART_BUTTON)
        await expect(main_menu.cart_counter_locator()).to_have_text("1")

        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await page.goto("https://practicesoftwaretesting.com")
