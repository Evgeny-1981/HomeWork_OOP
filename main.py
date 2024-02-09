from src.classes import Category
from utils.load_from_json import load_categorys, load_products

category = load_categorys()
product = load_products()

for item in category:
    print(item)

for item in product:
    print(item)

print(f"Количество категорий - {Category.quantity_category}")
print(f"Общее количество продуктов -{Category.quantity_uniq_product}")
