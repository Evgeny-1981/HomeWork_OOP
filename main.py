from src.classes import Product, SmartPhone, GrassLawn, Category
from utils.load_from_json import load_categorys

cat = load_categorys()
for i in cat:
    print(i)
# """Создаем категорию и два продукта"""
# cat1 = Category('TV', 'Новые телевизоры с технологией 3D', [])
# p1 = Product('Телевизор', 'LG', 10000, 1, 'red')
# p2 = Product('Телевизор', 'Philips', 18000, 1, 'red')
# p3 = Product('Телевизор', 'Sony-KDX55', 10000, 1, 'red')
#
# """Выведем средню стоимость при нулевом количестве товаров в категории"""
# print(cat1)
# ap = Category.average_price(cat1)
# print(ap)
#
# """Добавляем в cat1 товар p1"""
# cat1.add_product(p1)
# print(cat1)
# ap = Category.average_price(cat1)
# print(ap)
#
# """Добавляем в cat1 товар p2"""
# cat1.add_product(p2)
# print(cat1)
# ap = Category.average_price(cat1)
# print(ap)
#
# """Пытаемся добавить товар p3 в cat1 с нулевым количеством"""
# cat1.add_product(p3)
# print(cat1)
# ap = Category.average_price(cat1)
# print(ap)
