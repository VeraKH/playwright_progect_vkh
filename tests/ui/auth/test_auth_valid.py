import pytest
from playwright.async_api import expect, Page
from pages.auth_page import AuthPage
from data.auth_test_data import (
    valid_users,
    valid_admin,
    caps_look_email,
    small_and_caps_email,
)

class TestAuthValid:

    #1 Valid users can log in
    @pytest.mark.parametrize("user_data, expected_text", valid_users)
    @pytest.mark.asyncio
    async def test_auth_leads_to_account_page(self, main_page: Page, user_data, expected_text, main_menu):
        auth_page = AuthPage(main_page)

        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(main_menu.user_name_exists()).to_have_text(expected_text)

    # 2 Valid admin can log in
    @pytest.mark.parametrize("user_data, expected_text", valid_admin)
    @pytest.mark.asyncio
    async def test_auth_leads_to_user_account_page(self, main_page: Page, user_data, expected_text, admin_page):
        auth_page = AuthPage(main_page)

        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(admin_page.admin_title_locator()).to_have_text(expected_text)

    #3 ALL capslook in Email
    @pytest.mark.parametrize("user_data, expected_text", caps_look_email)
    @pytest.mark.asyncio
    async def test_all_caps_in_email(self, main_page: Page, user_data, expected_text, main_menu):
        auth_page = AuthPage(main_page)

        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(main_menu.user_name_exists()).to_have_text(expected_text)

    #4 Various register in Email
    @pytest.mark.parametrize("user_data, expected_text", small_and_caps_email)
    @pytest.mark.asyncio
    async def test_various_register_in_email(self, main_page: Page, user_data, expected_text, main_menu):
        auth_page = AuthPage(main_page)

        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(main_menu.user_name_exists()).to_have_text(expected_text)

