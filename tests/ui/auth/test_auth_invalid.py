import pytest
from playwright.async_api import expect, Page
from pages.auth_page import AuthPage
from data.auth_test_data import (
    invalid_email_data,
    invalid_password_data,
    invalid_email_and_password_data,
    empty_email_cases,
    empty_password_cases,
    empty_both_cases,
    caps_look_password,
    small_and_caps_password
)

class TestAuthInvalid:

    #1 Invalid email
    @pytest.mark.parametrize("user_data, expected_text", invalid_email_data)
    @pytest.mark.asyncio
    async def test_wrong_email_shows_message(self, main_page: Page, user_data, expected_text):
        auth_page = AuthPage(main_page)
        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(auth_page.login_error_locator()).to_have_text(expected_text)

    #2 Invalid password
    @pytest.mark.parametrize("user_data, expected_text", invalid_password_data)
    @pytest.mark.asyncio
    async def test_wrong_password_shows_message(self, main_page: Page, user_data, expected_text):
        auth_page = AuthPage(main_page)
        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(auth_page.login_error_locator()).to_have_text(expected_text)

    #3 Invalid password and email
    @pytest.mark.parametrize("user_data, expected_text", invalid_email_and_password_data)
    @pytest.mark.asyncio
    async def test_wrong_email_and_password_shows_message(self, main_page: Page, user_data, expected_text):
        auth_page = AuthPage(main_page)
        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(auth_page.login_error_locator()).to_have_text(expected_text)

    #4 Empty email
    @pytest.mark.parametrize("user_data, expected_text", empty_email_cases)
    @pytest.mark.asyncio
    async def test_empty_email_message(self, main_page: Page, user_data, expected_text):
        auth_page = AuthPage(main_page)
        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(auth_page.email_error_locator()).to_have_text(expected_text)

    # 4 Empty password
    @pytest.mark.parametrize("user_data, expected_text", empty_password_cases)
    @pytest.mark.asyncio
    async def test_empty_password_shows_message(self, main_page: Page, user_data, expected_text):
        auth_page = AuthPage(main_page)
        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(auth_page.password_error_locator()).to_have_text(expected_text)

    # 5 Empty password and email
    @pytest.mark.parametrize("user_data, expected_text_1, expected_text_2", empty_both_cases)
    @pytest.mark.asyncio
    async def test_empty_email_and_password_message(self, main_page: Page, user_data, expected_text_1, expected_text_2):
        auth_page = AuthPage(main_page)
        await auth_page.login(email=user_data["email"], password=user_data["password"])

        await expect(auth_page.email_error_locator()).to_have_text(expected_text_1)
        await expect(auth_page.password_error_locator()).to_have_text(expected_text_2)

    # 6 Empty password
    @pytest.mark.parametrize("user_data, expected_text", caps_look_password)
    @pytest.mark.asyncio
    async def test_caps_password_email_shows_message(self, main_page: Page, user_data, expected_text):
        auth_page = AuthPage(main_page)
        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(auth_page.login_error_locator()).to_have_text(expected_text)

    # 7 Empty password
    @pytest.mark.parametrize("user_data, expected_text", empty_password_cases)
    @pytest.mark.asyncio
    async def test_empty_password_shows_message(self, main_page: Page, user_data, expected_text):
        auth_page = AuthPage(main_page)
        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(auth_page.login_error_locator()).to_have_text(expected_text)

    #8 Various register in Password
    @pytest.mark.parametrize("user_data, expected_text", small_and_caps_password)
    @pytest.mark.asyncio
    async def test_caps_and_small_password_shows_message(self, main_page: Page, user_data, expected_text):
        auth_page = AuthPage(main_page)
        await auth_page.login(email=user_data["email"], password=user_data["password"])
        await expect(auth_page.login_error_locator()).to_have_text(expected_text)
