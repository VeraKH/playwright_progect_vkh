import pytest
from playwright.async_api import expect


class TestAuthenticatedSession:

    @pytest.mark.asyncio
    async def test_user_is_authenticated(self, authenticated_context):
        # Создаём страницу в авторизованном контексте
        page = await authenticated_context.new_page()

        # Переходим на страницу аккаунта
        await page.goto("https://practicesoftwaretesting.com/account")

        # Проверяем, что на странице присутствует имя пользователя 
        await expect(page.get_by_test_id("nav-menu")).to_have_text("Jane Doe")


        # Закрываем страницу после теста
        await page.close()