import pytest
from playwright.async_api import expect, Page

class TestProductGrid:

    @pytest.mark.asyncio
    async def test_home_page_products_count(self, page:Page):
        product_grid = page.locator(".col-md-9")
        # Check the count of products
        await expect(product_grid.get_by_role("link")).to_have_count(9)