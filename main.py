from utils.load_from_json import load_categorys, load_products
from src.classes import Category, Product



# list_categorys = load_categorys()
# list_products = load_products()

# new_product = Product('name', 'description', 'price', 'quantity_in_stock')
# print(new_product.name, new_product.description)

product = Product.new_product('name', 'description', 'price', 'quantity_in_stock')
# Product.new_product('name', 'description', 'price', 'quantity_in_stock')
add_product(product)


# res = Category.display_products_in_category
print(Category.output_products_in_category)

# for i in list_categorys:
#     print(i)
# print(list_products)

#
# print(len(list_categorys))
# print(len(list_products))
# #
