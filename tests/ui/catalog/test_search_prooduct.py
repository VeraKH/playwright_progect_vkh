import pytest
import asyncio
from playwright.async_api import expect, Page
from pages.catalog.search_bar_page import SearchBar
from pages.catalog.product_grid_page import CatalogPage

class TestSearchProduct:

    @pytest.mark.asyncio
    async def test_home_page_search_for_product(self, main_page: Page):
        search_bar = SearchBar(main_page)
        product_grid = CatalogPage(main_page)

        await search_bar.fill_data_in_input(search_bar.SEARCH_DATA)
        await search_bar.search_button_click()
        await product_grid.check_each_title_contains(search_bar.SEARCH_DATA)