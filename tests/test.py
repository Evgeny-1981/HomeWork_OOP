import pytest

from src.classes import Category, Product


@pytest.fixture()
def category_TV():
    return Category('ТВ, консоли и аудио',
                    'Телевизоры и аксессуары',
                    ['Телевизоры', 'Проекторы', 'Видеокабели'])


def test_category_init(category_TV):
    """Тест корректности инициализации объектов класса Category"""
    assert category_TV.name == 'ТВ, консоли и аудио'
    assert category_TV.description == 'Телевизоры и аксессуары'
    assert category_TV.products == ['Телевизоры', 'Проекторы', 'Видеокабели']

    """Тест подсчета количества продуктов и категорий"""
    assert Category.quantity_category == 1
    assert Category.quantity_uniq_product == 3


@pytest.fixture()
def product_TV():
    return Product('Телевизор',
                   'LED LG 32LM576BPLD',
                   22000, 10)


def test_product_init(product_TV):
    """Тест корректности инициализации объектов класса Product"""
    assert product_TV.name == 'Телевизор'
    assert product_TV.description == 'LED LG 32LM576BPLD'
    assert product_TV.price == 22000
    assert product_TV.quantity_in_stock == 10
