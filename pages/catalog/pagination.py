from playwright.async_api import Page, expect
import asyncio


class Pagination:
    def __init__(self, page: Page):
        self.page = page