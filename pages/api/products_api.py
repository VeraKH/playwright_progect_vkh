class ProductsAPI:

    def __init__(self, api_request_context):
        self.api = api_request_context

    # Get status code for all brands and return all products json
    async def get_all_categories(self):
        response = await self.api.get("/categories")
        assert response.status == 200
        return await response.json()
    
    # Get status code for all categories and return all categories json
    async def get_all_brands(self):
        response = await self.api.get("/brands")
        assert response.status == 200
        return await response.json()
    
    # Get status code for all products and return all products json
    async def get_all_products(self):
        response = await self.api.get("/products")
        assert response.status == 200
        return await response.json()

    async def get_products_with_optional_filters(
            self,
            price_min=None,
            price_max=None,
            category_id=None,
            brand_id=None
    ):

        filters = []

        # Добавляем фильтры
        if price_min is not None and price_max is not None:
            filters.append(f"between=price,{price_min},{price_max}")
        elif price_min is not None:
            filters.append(f"between=price,{price_min}")
        elif price_max is not None:
            filters.append(f"between=price,0,{price_max}")

        if brand_id:
            filters.append(f"by_brand={brand_id}")

        if category_id:
            filters.append(f"by_category={category_id}")

        # Добавим page=0 в любом случае
        filters.append("page=0")

        # Склеиваем параметры
        query = "&".join(filters)

        # Строим URL
        url = f"/products?{query}"

        response = await self.api.get(url)
        assert response.status == 200
        products_json = await response.json()
        products = products_json["data"]

        return products


    async def get_category_by_name(self, name: str):
        # Получаем все категории
        all_categories = await self.get_all_categories()

        # Фильтруем категории по имени
        filtered_categories = [cat for cat in all_categories if cat["name"].lower() == name.lower()]

        # Если категория найдена, возвращаем её, иначе выбрасываем исключение
        if filtered_categories:
            return filtered_categories[0]  # Возвращаем первую подходящую категорию
        else:
            raise ValueError(f"Category with name '{name}' not found")

    async def get_category_id_by_name(self, name: str) -> str:
        all_categories = await self.get_all_categories()
        for cat in all_categories:
            if cat["name"].lower() == name.lower():
                return cat["id"]
        raise ValueError(f"Category '{name}' not found")

    
    async def get_brand_name_by_id(self, name: str):
        data = await self.get_all_brands()

        for brand in data:
            if brand["name"] == name:
                return brand["id"]
        raise ValueError(f"Brand '{name}' is not found")

    