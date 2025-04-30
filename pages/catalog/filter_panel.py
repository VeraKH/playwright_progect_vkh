from playwright.async_api import Page, expect

class FilterPanel:

    PRODUCT_NAME = '[data-test="product-name"]'

    def __init__(self, page: Page):
        self.page = page

    def return_all_check_boxes(self):
        return self.page.get_by_role("checkbox")

    async def get_checkbox_by_category_name(self, category_name: str):
        return self.page.get_by_label(category_name)

    async def click_on_category(self, category_name: str):
        checkbox = await self.get_checkbox_by_category_name(category_name)

        # Ожидание API-респонса начинается до клика
        async with self.page.expect_response(lambda r: "/products?" in r.url and r.status == 200):
            await checkbox.click()

        # UI уже может безопасно рендериться
        await expect(self.page.locator("[data-test='product-name']").last).to_be_visible()

    async def return_all_product_names_in_results(self):
        products_in_result = self.page.get_by_test_id(self.PRODUCT_NAME).all_text_contents()
        return products_in_result




