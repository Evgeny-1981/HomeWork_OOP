from src.classes import Category, Product
from utils.load_from_json import load_categorys, load_products

category = load_categorys()
product = load_products()

print(category)
print(product)
