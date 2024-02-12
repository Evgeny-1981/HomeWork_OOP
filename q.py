import json
from pathlib import Path

from src.classes import Category

FILE_NAME = Path("utils", "products.json")
with open(FILE_NAME, 'r', encoding='utf8') as f:
    data = json.load(f)
    category_list = []
    product_list = []

category = Category('name',
                    'description',
                    'products')
print(Category.products)
category_list.append(category)
# return category_list


for category in category_list:
    print(f"{product_list},  рублей. Остаток: ")
