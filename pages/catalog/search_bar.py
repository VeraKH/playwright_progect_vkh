from playwright.async_api import Page, expect


class SearchBar:
    SEARCH_INPUT = '[data-test="search-query"]'
    SEARCH_DATA = 'Pliers'
    STATUS_ENDPOINT = "https://api.practicesoftwaretesting.com/products/search?"

    def __init__(self, page: Page):
        self.page = page

    def search_bar_locator(self):
        return self.page.locator(self.SEARCH_INPUT)

    async def fill_data_in_input(self, data: str):
        await self.search_bar_locator().fill(data)

    def search_button_locator(self):
        return self.page.get_by_role("button", name="Search")

    async def search_button_click(self):
        button = self.search_button_locator()
        async with self.page.expect_response(lambda r: "/products/search" in r.url and r.status == 200):
            await button.click()






