import pytest
from playwright.async_api import expect, Page
from pages.catalog.filter_panel import FilterPanel
from pages.api.products_api import ProductsAPI
from pages.catalog.product_grid import CatalogPage

class TestFilter:

    @pytest.mark.asyncio
    async def test_filter_by_category(self, page:Page, api_request_context):

        products_api = ProductsAPI(api_request_context)
        filter_ui = FilterPanel(page)
        catalog = CatalogPage(page)

        selected_category = "Pliers"

        category_id = await products_api.get_category_id_by_name(selected_category)
        print(category_id)
        # Получаем все продукты для выбранной категории через API
        products_api = await products_api.get_products_with_optional_filters(category_id=category_id, price_max=100)

        await filter_ui.click_on_category(selected_category)

        # 3. Получаем продукты из UI
        ui_product_titles = await catalog.get_lower_case_titles_from_ui()

        # Сравниваем товары по названиям
        for product in products_api:
            product_name_api = product['name'].lower()  # Приводим к нижнему регистру
            assert product_name_api in ui_product_titles, \
                f"Product {product_name_api} from API is not found in UI under category {selected_category}"





