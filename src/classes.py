from abc import ABC, abstractmethod


class AbstractCategory(ABC):
    """Создаем абстрактный класс для класса Category"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Mixin:
    """Создаем класс для вывода информации о созданном объекте"""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f'Создан объект класса {self.__class__.__name__} с атрибутами: {self.__dict__}'


class Category(Mixin, AbstractCategory):
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
        super().__init__()

        Category.quantity_category += 1
        Category.quantity_uniq_product += len(self.__products)

    def add_product(self, product):
        """Метод принимает на вход объект товара и добавляет его в список"""
        if not isinstance(product, Product):
            raise TypeError('Нельзя добавлять в список объекты, кроме объектов Product и его наследников')
        else:
            self.__products.append(product)

    @property
    def output_products_in_category(self):
        """Для атрибута класса Category «товары» создаем геттер, который будет выводить список товаров в формате:
        Продукт, XX руб. Остаток: XX шт."""
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity_in_stock} шт."
                for product in self.__products]

    def __len__(self):
        """Подсчет общего числа продуктов на складе"""
        return len(self.__products)

    def __str__(self):
        """Добавляем строковое отображение в следующем виде:
        Название категории, количество продуктов: XX шт."""
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __repr__(self):
        return super().__repr__()


class AbstractProduct(ABC):
    """Создаем абстрактный класс для классов Product, SmartPhone, GrassLawn"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def create_product(self):
        pass


class Product(Mixin, AbstractProduct):
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
        super().__init__()

    def __add__(self, other):
        """Складваем объекты между собой.
        Результат это сумма произведений стоимости на количество товара на складе"""
        if type(self) is not type(other):
            raise TypeError('Нельзя складывать товары разных типов')
        total = self.price * self.quantity_in_stock + other.price * other.quantity_in_stock
        return total

    def __str__(self):
        """ Создаем строковое отображение в следующем виде: Название продукта, ХХ руб. Остаток: ХХ шт."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт."

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock, color=None):
        """Метод создает новый товар и вовращает объект, который можно добавить в список"""
        product = cls(name, description, price, quantity_in_stock, color=None)
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

    def __repr__(self):
        return super().__repr__()


class SmartPhone(Product):
    """Создание дочернего класса 'Смартофон'"""
    efficiency: float  # производитеьность
    model: str  # модель
    volume_ram: int  # объем встроенной памяти

    def __init__(self, name, description, price, quantity_in_stock, color, efficiency, model, volume_ram):
        super().__init__(name, description, price, quantity_in_stock, color)
        self.efficiency = efficiency
        self.model = model
        self.volume_ram = volume_ram


class GrassLawn(Product):
    """Создание дочернего класса 'Трава газонная'"""
    country_origin: str  # страна-производитель
    germ_period: int  # срок прорастания

    def __init__(self, name, description, price, quantity_in_stock, color, country_origin, germ_period):
        super().__init__(name, description, price, quantity_in_stock, color)
        self.country_origin = country_origin
        self.germ_period = germ_period
