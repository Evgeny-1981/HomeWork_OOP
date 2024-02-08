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


if __name__ == '__main__':
    cat1 = Category('Видеотехника', 'qwert', ['tele1', 'tele2', 'tele3'])
    cat2 = Category('Видеотехника', 'qwert', ['tele1', 'tele1', 'tele1', 'tele7', 'tele8'])
    cat3 = Category('Видеотехника', 'qwert', ['tele1', 'tele2', 'tele4'])

    print(cat1)
    print(cat1.name)
    print(cat1.description)
    print(cat1.products)
    print()
    print(cat2)
    print(cat2.name)
    print(cat2.description)
    print(cat2.products)
    print()
    print(cat3)
    print(cat3.name)
    print(cat3.description)
    print(cat3.products)
    print()
    print(Category.quantity_category)
    print(Category.quantity_uniq_product)
