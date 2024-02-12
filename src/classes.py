class Category:
    """Создаем класс Category"""
    name: str
    description: str
    products: list
    """Добавляем два атрибута, в которых будут храниться общее
    количество категорий и общее количество уникальных продуктов,
    не учитвая количество в наличии"""
    quantity_category = 0
    quantity_uniq_product = 0

    def __init__(self, name, description, products):
        """Инииализируем объект класса Category"""
        self.name = name
        self.description = description
        self.products = products

        Category.quantity_category += 1
        Category.quantity_uniq_product += len(self.products)

    def add_product(self, product):
        """Метод создает новый товар и вовращает объект, который можно добавить в список"""
        self.products.append(product)

    @property
    def output_products_in_category(self):
        """Для атрибута класса Category «товары» создаем геттер, который будет выводить список товаров в формате:
        Продукт, 80 руб. Остаток: 15 шт."""
        for product in self.products:
            return list(f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт.")


class Product:
    """Создаем класс Product"""
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        """Инииализируем объект класса Product"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock):
        """Метод создает новый товар и вовращает объект, который можно добавить в список"""
        product = cls(name, description, price, quantity_in_stock)
        return product

    @property
    def get_price(self):
        return self.price

    @get_price.setter
    def get_price(self, new_price):
        self.price = self.check_price(new_price)

    @staticmethod
    def check_price(new_price):
        if new_price <= 0:
            return "Введена не корректная цена!"
        elif new_price < Product.get_price:
            if input("Подтвердите понижение цены на товар: Y/N (Y - да, N - нет): ").isalpha() == "y" or "Y":
                return new_price
        else:
            return new_price
