import pytest
import asyncio
from playwright.async_api import expect, Page
from pages.catalog.search_bar import SearchBar
from pages.catalog.product_grid import CatalogPage

class TestSearchProduct:

    @pytest.mark.asyncio
    async def test_home_page_search_for_product(self, page: Page):
        search_bar = SearchBar(page)
        product_grid = CatalogPage(page)

        await search_bar.fill_data_in_input(search_bar.SEARCH_DATA)
        await search_bar.search_button_click()
        await product_grid.check_each_title_contains(search_bar.SEARCH_DATA)