import json
from pathlib import Path

from src.classes import Category, Product

FILE_NAME = Path("utils", "products.json")
with open(FILE_NAME, 'r', encoding='utf8') as f:
    data = json.load(f)
    category_list = []
    product_list = []

for category in data:
    # print(category)
    new_category = Category('name',
                        'description',
                        'products')
    print(new_category)
    category_list.append(new_category)
# for category in category_list:
#     print(category)


# for product in data:
#     for product in product['products']:
#         print(product)
#         new_product = Product('name',
#                           'description',
#                           "price",
#                           'quantity')
#         product_list.append(new_product)

