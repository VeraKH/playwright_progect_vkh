import pytest
from playwright.async_api import expect, Page
from pages.main_menu import MainMenu


class TestHomePageMenu:

    # Ensure the Sign In-link is present
    @pytest.mark.asyncio
    async def test_sign_up_link_exists(self, page: Page):
        main_menu = MainMenu(page)
        await expect(main_menu.sign_in_link_exists()).to_have_text("Sign in")
