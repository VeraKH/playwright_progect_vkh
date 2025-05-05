import pytest
from playwright.async_api import expect, Page


class TestAuthentication:

    @pytest.mark.asyncio
    async def test_user_can_go_to_account_page(self, page: Page, store_authenticated_state):
        # Получаем контекст с авторизованным состоянием
        context = store_authenticated_state

        # Создаем новую страницу в этом контексте
        page = await context.new_page()

        # Переходим на страницу аккаунта
        await page.goto("https://practicesoftwaretesting.com/account")

        # Закрываем страницу после теста
        await page.close()
