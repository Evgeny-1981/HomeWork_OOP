from utils.load_from_json import load_categorys, load_products
from src.classes import Category, Product


list_categorys = load_categorys()
list_products = load_products()

new_product = Category.new_product("Test", "Test description",  ['q','r'])
print(new_product.name, new_product.description, new_product.products)
list_categorys.append(new_product)

print(list_categorys)
print(list_products)



print(len(list_categorys))
print(len(list_products))
#
