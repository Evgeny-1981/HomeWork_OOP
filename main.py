from src.classes import Product, SmartPhone, GrassLawn, Category

p1 = Product('Телевизор', 'новейший', 10000, 2, 'red')
s1 = SmartPhone('Смартфон', 'Новейший', 20000, 2, 'blue', 2, 'Realme', 128)
g1 = GrassLawn('Трава', 'Зеленая', 1000, 2, 'Green', 'RUS', 3)
cat1 = Category('TV', 'Новые телевизоры с технологией 3D', [p1])
print(cat1.__repr__())
print(p1.__repr__())
print(s1.__repr__())
print(g1.__repr__())
print(f'Всего категорий: {cat1.quantity_category}')
print(f'Всего продуктов в категории {cat1.name}: {cat1.quantity_uniq_product}')
print(f'Наменование продуктов в категории {cat1.name}: {cat1.output_products_in_category}')
