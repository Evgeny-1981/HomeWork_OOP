import json
import pathlib
import os

from main import Category, Product

path = pathlib.Path("data/products.json")
with open(path, 'r', encoding='utf8') as f:
    data = json.load(f)

    for category in data:
        category = Category(category['name'], category['description'], category['products'])
        print(category.products)

