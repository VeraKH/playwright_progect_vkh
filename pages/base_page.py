from playwright.async_api import Page, expect

class BasePage:

    EXPECTED_TITLE_HOME = "Practice Software Testing - Toolshop - v5.0"
    BASE_URL = "https://practicesoftwaretesting.com/"

    def __init__(self, page: Page):
        self.page = page

    async def go_to_main_page(self):
        await self.page.goto(self.BASE_URL)
        await self.page.wait_for_load_state("networkidle")

    async def check_element_visible(self, locator_str: str):
        element = self.page.locator(locator_str)
        await expect(element).to_be_visible()

    async def check_page_title(self, expected_title: str):
        await expect(self.page).to_have_title(expected_title)