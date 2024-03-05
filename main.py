from src.classes import Product, SmartPhone, GrassLawn, Category

"""Создаем категорию и два продукта"""
cat1 = Category('TV', 'Новые телевизоры с технологией 3D', [])
p1 = Product('Телевизор', 'LG', 10000, 1, 'red')
p2 = Product('Телевизор', 'Philips', 18000, 1, 'red')
p3 = Product('Телевизор', 'Sony-KDX55', 100000, 0, 'red')

"""Добавляем в cat1 товар p1"""
cat1.add_product(p1)
print(cat1)
ap = Category.average_price(cat1)
print(ap)

"""Добавляем в cat1 товар p2"""
cat1.add_product(p2)
print(cat1)
ap = Category.average_price(cat1)
print(ap)

"""Пытаемся добавить товар p3 в cat1 с нулевым количеством"""
cat1.add_product(p3)
print(cat1)
ap = Category.average_price(cat1)
print(ap)
