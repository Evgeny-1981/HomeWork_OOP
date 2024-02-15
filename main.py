from src.classes import Product, Category

product = Product.create_product('new product', 'Create new product', 10, 1)
a = Category.add_product('asd asd')
cat = Category.output_products_in_category
print(product.name, product.description, product.price, product.quantity_in_stock)
print(a)
print(Category.output_products_in_category)
