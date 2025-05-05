from playwright.async_api import Page, expect

class FilterPanel:

    # CSS selector for product names in the UI
    PRODUCT_NAME = '[data-test="product-name"]'

    def __init__(self, page: Page):
        self.page = page

    # Return all checkboxes on the filter panel
    def return_all_check_boxes(self):
        return self.page.get_by_role("checkbox")

    # Find and return the checkbox for the given category name
    async def get_checkbox_by_category_name(self, category_name: str):
        return self.page.get_by_label(category_name)

    # Locate the checkbox for the selected category
    async def click_on_category(self, category_name: str):
        checkbox = await self.get_checkbox_by_category_name(category_name)

        # Step 1: Start waiting for a response from the API before clicking the checkbox
        # We're listening for a network response that contains products (with a status of 200)
        async with self.page.expect_response(lambda r: "/products?" in r.url and r.status == 200):
            await checkbox.click()

        # Step 2: After clicking the checkbox, ensure that the product names are visible in the UI
        # The UI rendering can proceed safely after the response is received
        await expect(self.page.locator("[data-test='product-name']").last).to_be_visible()

    # Get the names of all products currently displayed in the search results
    # We use the PRODUCT_NAME selector defined earlier
    async def return_all_product_names_in_results(self):
        products_in_result = self.page.get_by_test_id(self.PRODUCT_NAME).all_text_contents()
        return products_in_result




