import asyncio
import pytest_asyncio
from playwright.async_api import async_playwright, expect, APIRequestContext
import os
from pages.auth_page import AuthPage
from pages.main_menu_page import MainMenu
from pages.admin_page import AdminPage

# Фикстура для event_loop с скоупом session
@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()  # создаём новый цикл событий
    yield loop  # возвращаем цикл событий в тесты
    loop.close()  # закрываем цикл после завершения тестов


# Асинхронная фикстура для Playwright
@pytest_asyncio.fixture(scope="session")
async def playwright():
    async with async_playwright() as playwright:
        yield playwright


# Фикстура для конфигурации селекторов
@pytest_asyncio.fixture(scope="session")
async def configure_selectors(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


# Фикстура для браузера
@pytest_asyncio.fixture(scope="session")
async def browser(playwright, configure_selectors):
    browser = await playwright.chromium.launch(headless=False)
    yield browser
    await browser.close()


# Фикстура для контекста браузера (с скоупом class)
@pytest_asyncio.fixture(scope="class")
async def browser_context(browser):
    context = await browser.new_context()
    yield context
    await context.close()


# Фикстура для страницы (с скоупом class)
@pytest_asyncio.fixture(scope="class")
async def page(browser_context):
    page = await browser_context.new_page()
    await page.goto("https://practicesoftwaretesting.com/")  # Загружаем сайт один раз
    await page.wait_for_load_state("networkidle")    
    
    yield page
    await page.close()


# Фикстура для сохранения состояния сессии (просто авторизация)
@pytest_asyncio.fixture(scope="function")
async def store_authenticated_state(browser):
    user_01_email = "customer@practicesoftwaretesting.com"
    user_01_password = "welcome01"

    # Создаем новый контекст браузера для авторизации
    context = await browser.new_context()

    # Открываем страницу авторизации
    page = await context.new_page()

    await page.goto("https://practicesoftwaretesting.com/")  # Загружаем сайт
    await page.get_by_test_id("nav-sign-in").click()

    # Заполняем форму авторизации
    await page.get_by_placeholder("Your email").fill(user_01_email)
    await page.get_by_placeholder("Your password").fill(user_01_password)
    await page.get_by_test_id("login-submit").click()

    # Ждем, пока не загрузится страница аккаунта
    await expect(page.get_by_test_id("nav-menu")).to_have_text("Jane Doe")

    # Сохраняем состояние (cookies и localStorage)
    storage_path = "playwright/.auth/customer01.json"

    os.makedirs(os.path.dirname(storage_path), exist_ok=True)
    await context.storage_state(path="playwright/.auth/customer01.json")

    # Возвращаем контекст с авторизованной сессией
    yield context

    # Закрываем контекст после теста
    await context.close()

@pytest_asyncio.fixture(scope="function")
async def authenticated_context(browser):
    # Check if there is a saved session
    storage_path = "playwright/.auth/customer01.json"
    if not os.path.exists(storage_path):
        raise FileNotFoundError(
            f"Auth state not found at {storage_path}. Run the session initializer test first."
        )

    context = await browser.new_context(storage_state=storage_path)
    yield context
    await context.close()



@pytest_asyncio.fixture(scope="session")
async def api_request_context(playwright):
    request_context = await playwright.request.new_context(
        base_url = "https://api.practicesoftwaretesting.com"  # Базовый URL
    )
    yield request_context
    await request_context.dispose()

@pytest_asyncio.fixture
async def logged_in_auth_page(page):
    auth_page = AuthPage(page)
    await auth_page.open_login_page()
    await auth_page.login(email="user@example.com", password="Password123")
    return auth_page


@pytest_asyncio.fixture
async def main_menu(page):
    return MainMenu(page)

@pytest_asyncio.fixture
async def admin_page(page):
    return AdminPage(page)

@pytest_asyncio.fixture
async def auth_page(page):
    return AuthPage(page)