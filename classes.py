class Category:
    name: str
    description: str
    products: list
    quantity_category = 0
    quantity_uniq_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.quantity_category += 1
        Category.quantity_uniq_product += len(self.products)


class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock