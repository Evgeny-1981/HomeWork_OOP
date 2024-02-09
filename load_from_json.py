import json
import pathlib

from classes import Category, Product

path = pathlib.Path("data/products.json")
with open(path, 'r', encoding='utf8') as f:
    data = json.load(f)
    category_list = []
    product_list = []


def load_categorys():
    for item in data:
        category = Category('name', 'description', 'products')
        category_list.append(category)
    return category_list


def load_products():
    for item in data:
        for prod in item['products']:
            product = Product('name', 'description', "price", 'quantity')
            product_list.append(product)
    return product_list
