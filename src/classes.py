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

    @classmethod
    def new_product(cls, name, description, products):
        """Метод создает новый товар и вовращает объект, который можно добавить в список"""
        new_product = cls(name, description, products)
        return new_product

    @property
    def display_products_in_category(self):
        for products in Category.products:
            res = f"{products[0]}, {products[1]} рублей. Остаток: {products[2]} штук"
        return res

    # def __repr__(self, res=None):
    #     pass

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

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def new_product(cls, name, description, price, quantity_in_stock):
        """Метод создает новый товар и вовращает объект, который можно добавить в список"""
        new_product = cls(None,
                          None,
                          0.0,
                          0)
        return new_product

    @staticmethod
    def chek_attr(name, description, price, quantity_in_stock):
        pass

# c1 = Category("jhvjh", "jkjbjb", ['y','2','r','y'])
# print(c1)