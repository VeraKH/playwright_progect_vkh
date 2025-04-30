from playwright.async_api import Page

class AuthPage:

    LOGIN_ERROR = "login-error"
    EMAIL_ERROR = "email-error"
    PASSWORD_ERROR = "password-error"

    def __init__(self, page: Page):
        self.page = page

    async def open_login_page(self):
        await self.page.goto("https://practicesoftwaretesting.com/auth/login")

    async def fill_email(self, email: str):
        await self.page.get_by_test_id("email").fill(email)

    async def fill_password(self, password: str):
        await self.page.get_by_test_id("password").fill(password)

    async def click_login_btn(self):
        await self.page.get_by_test_id("login-submit").click()

    def login_error_locator(self):
        return self.page.get_by_test_id(self.LOGIN_ERROR)

    def email_error_locator(self):
        return self.page.get_by_test_id(self.EMAIL_ERROR)

    def password_error_locator(self):
        return self.page.get_by_test_id(self.PASSWORD_ERROR)

    async def login(self, email: str, password: str):
        await self.open_login_page()
        await self.fill_email(email)
        await self.fill_password(password)
        await self.click_login_btn()
