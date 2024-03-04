from src.classes import Product, SmartPhone, GrassLawn, Category

cat1 = Category('TV', 'Новые телевизоры с технологией 3D', [])
p1 = Product('Телевизор', 'LG', 10000, 1, 'red')
p2 = Product('Телевизор', 'Philips', 18000, 10, 'red')
p3 = Product('Телевизор', 'Sony-KDX55', 100000, 1, 'red')

cat1.add_product(p1)
print(cat1)

cat1.add_product(p2)
# print(cat1.__len__())
print(cat1)
# cat1.add_product(p3)
# print(cat1.__len__())

ap = Category.average_price(cat1)
print(ap)

# s1 = SmartPhone('Смартфон', 'Новейший', 20000, 2, 'blue', 2, 'Realme', 128)
# g1 = GrassLawn('Трава', 'Зеленая', 1000, 2, 'Green', 'RUS', 3)
# p2 = Product.create_product('Телевизор', 'швейная', 1500, 3, 'black')
