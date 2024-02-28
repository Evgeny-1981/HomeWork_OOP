from src.classes import Product, SmartPhone, GrassLawn, Category

p1 = Product('Телевизор', 'новейший', 10000, 2, 'red')
s1 = SmartPhone('Смартфон', 'Новейший', 20000, 2, 'blue', 2, 'Realme', 128)
g1 = GrassLawn('Трава', 'Зеленая', 1000, 2, 'Green', 'RUS', 3)
cat1 = Category('TV', 'Новые телевизоры с технологией 3D', [p1])

p2 = Product.create_product('Телевизор', 'швейная', 1500, 3, 'black')


