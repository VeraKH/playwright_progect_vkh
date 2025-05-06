from playwright.async_api import Page, expect

class ProductGrid:
    PRODUCT_TITLE = '[data-test="product-name"]'

    def __init__(self, page: Page):
        self.page = page

    def get_product_titles_locator(self):
        return self.page.locator(self.PRODUCT_TITLE)

    async def click_product_by_name(self, product_name: str):
        product_to_click = self.page.locator(self.PRODUCT_TITLE).filter(has_text=product_name)
        await product_to_click.first.click()

    # Counts products
    async def count_product_names(self):
        products_displayed = self.page.locator(self.PRODUCT_TITLE)
        number = await products_displayed.count()
        return number

    # Приводим в нижний регистр для сравнения все названия товаров
    async def get_lower_case_titles_from_ui(self):
        product_elements = await self.page.locator(self.PRODUCT_TITLE).all()

        product_titles = []
        for product_element in product_elements:
            title = await product_element.text_content()
            product_titles.append(title.strip().lower())

        return product_titles

    # Проверяет, что все названия товаров содержат нужное слово
    async def check_each_title_contains(self, expected_text: str):
        titles_locator = self.page.locator(self.PRODUCT_TITLE)
        count = await titles_locator.count()
        for i in range(count):
            await expect(titles_locator.nth(i)).to_contain_text(expected_text)