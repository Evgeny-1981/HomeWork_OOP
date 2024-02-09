import json
import pathlib
import os

from main import Category, Product

path = pathlib.Path("data/products.json")
with open(path, 'r', encoding='utf8') as f:
    data = json.load(f)
    list_cat = []
    list_prod = []

    for item in data:
        category = Category(item['name'], item['description'], item['products'])
        list_cat.append(category)
    print(list_cat)
    print(Category.quantity_category)
    for item in data:
        product = Product(item['name'], ['description'], ['price'], ['quantity'])
        list_prod.append(product)
    print(list_prod)


