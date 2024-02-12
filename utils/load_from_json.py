import json
from pathlib import Path

from src.classes import Category, Product

# BASE_DIR = Path(__file__).parent
# FILE_NAME = Path(BASE_DIR, "products.json")
# with open(FILE_NAME, 'r', encoding='utf8') as f:
#     data = json.load(f)
#     category_list = []
#     product_list = []


def load_categorys():
    """Загрузка категорий из файла"""
    BASE_DIR = Path(__file__).parent
    FILE_NAME = Path(BASE_DIR, "products.json")
    with open(FILE_NAME, 'r', encoding='utf8') as f:
        data = json.load(f)
        category_list = []
        product_list = []

    for item in data:
        category = Category('name',
                            'description',
                            'products')
        category_list.append(category)
    return category_list


def load_products():
    """Загрузка продуктов из файла"""
    BASE_DIR = Path(__file__).parent
    FILE_NAME = Path(BASE_DIR, "products.json")
    with open(FILE_NAME, 'r', encoding='utf8') as f:
        data = json.load(f)
        category_list = []
        product_list = []

    for item in data:
        for prod in item['products']:
            product = Product('name',
                              'description',
                              "price",
                              'quantity')
            product_list.append(product)
    return product_list
