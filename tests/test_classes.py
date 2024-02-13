import pytest

from src.classes import Category, Product


@pytest.fixture()
def category_tv():
    return Category('ТВ, консоли и аудио',
                    'Телевизоры и аксессуары',
                    ['Телевизоры', 'Проекторы', 'Видеокабели'])


def test_category_init(category_tv):
    """Тест корректности инициализации объектов класса Category"""
    assert category_tv.name == 'ТВ, консоли и аудио'
    assert category_tv.description == 'Телевизоры и аксессуары'
    # assert category_tv.products == ['Телевизоры', 'Проекторы', 'Видеокабели']

    """Тест подсчета количества продуктов и категорий"""
    assert Category.quantity_category == 1
    assert Category.quantity_uniq_product == 3


@pytest.fixture()
def product_tv():
    return Product('Телевизор',
                   'LED LG 32LM576BPLD',
                   22000, 10)


def test_product_init(product_tv):
    """Тест корректности инициализации объектов класса Product"""
    assert product_tv.name == 'Телевизор'
    assert product_tv.description == 'LED LG 32LM576BPLD'
    assert product_tv.price == 22000
    assert product_tv.quantity_in_stock == 10
