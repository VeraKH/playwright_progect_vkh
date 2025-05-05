import pytest
from playwright.async_api import expect, Page
from pages.catalog.filter_panel_page import FilterPanel
from pages.api.products_api import ProductsAPI
from pages.catalog.product_grid_page import CatalogPage

class TestFilter:

    @pytest.mark.asyncio
    async def test_filter_by_category(self, main_page: Page, api_request_context):

        # Initialize API and UI helper objects
        products_api = ProductsAPI(api_request_context)
        filter_ui = FilterPanel(main_page)
        catalog = CatalogPage(main_page)

        # Step 1: Define the category to be tested
        selected_category = "Pliers"

        # Step 2: Get the category ID for "Pliers" from API
        category_id = await products_api.get_category_id_by_name(selected_category)
        print(category_id)

        # Step 3: Get products from API filtered by category and price
        products_from_api = await products_api.get_products_with_optional_filters(
            category_id=category_id, price_max=100
        )

        # Step 4: Apply category filter in UI
        await filter_ui.click_on_category(selected_category)

        # Step 5: Get list of product titles displayed in the UI
        ui_product_titles = await catalog.get_lower_case_titles_from_ui()

        # Step 6: Compare product titles from API with UI to ensure they match
        for product in products_from_api:
            product_name_api = product['name'].lower()  # normalize for case-insensitive match
            assert product_name_api in ui_product_titles, \
                f"Product {product_name_api} from API is not found in UI under category {selected_category}"
