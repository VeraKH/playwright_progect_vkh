import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
class TestApi:

    async def test_post_auth(self, api_request_context):
        payload = {
            "email": "customer@practicesoftwaretesting.com",
            "password": "welcome01"
        }
        response = await api_request_context.post("/users/login	", data=payload)  # Запрос к API
        assert response.status == 200
        
        body = await response.json()

        assert "access_token" in body
        assert isinstance(body["access_token"], str)
        assert body["access_token"] != ""  # Убедись, что токен не пустой

    async def test_get_products(self, api_request_context):
        response = await api_request_context.get("/products")  # Запрос к API
        assert response.status == 200  # Проверяем, что сервер отвечает 200
        body = await response.json()
        # Проверяем, что поле "data" существует и в нём 9 элементов
        assert "data" in body
        assert isinstance(body["data"], list)
        assert len(body["data"]) == 9
        assert body["total"] == 50

