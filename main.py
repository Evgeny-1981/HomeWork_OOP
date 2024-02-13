from src.classes import Category, Product

# product1 = Product('Новый проддукт', 'Описание продукта', 5885, 5)
product = Product.create_product('Новый продукт 2', 'wee', 35165, 9)
Category.add_product('sdfdsf', '[1, 2, 3]')
# print(category.output_products_in_category)

# Category.output_products_in_category
print(product.name)
print(product.get_price)
product.get_price = 150000.0
print(product.get_price)
print(category.output_products_in_category)
