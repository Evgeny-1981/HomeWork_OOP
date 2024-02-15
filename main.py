
from src.classes import Product, Category

prod = ["TV", "TVnew", 150]
# category1 = Category.add_product(Category, 'dfhfdhdh')
product1 = Product.create_product('Телевизор', 'Крутой', 10000, 2)

print(product1)
print(Category.output_products_in_category)
# print(category1)