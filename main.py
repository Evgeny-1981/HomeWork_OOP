from src.classes import Category
from utils.load_from_json import load_categorys, load_products

category = load_categorys()  # Получаем список категорий
product = load_products()  # Получаем список продуктов

print(category)
print(product)
