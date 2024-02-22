class Category:
    """Создаем класс Category!"""
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
        self.__products = products

        Category.quantity_category += 1
        Category.quantity_uniq_product += len(self.__products)

    def add_product(self, product):
        """Метод создает новый товар и вовращает объект, который можно добавить в список"""
        if not isinstance(product, Product):
            raise TypeError('Нельзя добавлять в список объекты, кроме объектов Product и его наследников')
        else:
            self.__products.append(product)

    @property
    def output_products_in_category(self):
        """Для атрибута класса Category «товары» создаем геттер, который будет выводить список товаров в формате:
        Продукт, XX руб. Остаток: XX шт."""
        for product in self.__products:
            return [f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт." for product in
                    self.__products]

    def __len__(self):
        """Подсчет общего числа продуктов на складе"""
        return len(self.__products)

    def __str__(self):
        """Добавляем строковое отображение в следующем виде:
        Название категории, количество продуктов: XX шт."""
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."


class Product:
    """Создаем класс Product"""
    name: str
    description: str
    price: float
    quantity_in_stock: int
    color: str

    def __init__(self, name, description, price, quantity_in_stock, color=None):
        """Инииализируем объект класса Product"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.color = color

    def __str__(self):
        """ Создаем строковое отображение в следующем виде: Название продукта, ХХ руб. Остаток: ХХ шт."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт."

    def __add__(self, other):
        """Складваем объекты между собой.
        Результат это сумма произведений стоимости на количество товара на складе"""
        if not isinstance(other, Product):
            raise ValueError('Ошибка')
        total = self.price * self.quantity_in_stock + other.price * other.quantity_in_stock
        return total


    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock):
        """Метод создает новый товар и вовращает объект, который можно добавить в список"""
        product = cls(name, description, price, quantity_in_stock)
        return product

    @property
    def get_price(self):
        """Геттер для атрибута цены"""
        return self.price

    @get_price.setter
    def get_price(self, new_price):
        """Сеттер для атрибута цены. Если новая цена равна или нижу ноля, то выводим сообщение о некорректности.
        Иначе запрашиваем разрешение, если цена ниже текущей и записываем новую цену на товар"""
        if new_price <= 0 or not isinstance(new_price, float):
            print("Введена некорректная цена!")
        elif new_price <= self.price:
            user_input = input("Подтвердите понижение цены на товар: Y/N (Y - да, N - нет): ")
            if user_input.lower() == 'y':
                self.price = new_price
        else:
            self.price = new_price


class SmartPhone(Product):
    """Создание дочернего класса 'Смартофон'"""

    def __init__(self, name, description, price, quantity_in_stock, color, efficiency, model, volume_ram):
        super().__init__(name, description, price, quantity_in_stock, color)
        self.efficiency = efficiency
        self.model = model
        self.volume_ram = volume_ram


class GrassLawn(Product):
    """Создание дочернего класса 'Трава газонная'"""

    def __init__(self, name, description, price, quantity_in_stock, color, country_origin, germ_period):
        super().__init__(name, description, price, quantity_in_stock, color)
        self.country_origin = country_origin
        self.germ_period = germ_period
