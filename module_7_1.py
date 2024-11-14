class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name

    def get_products(self):
        file = open(self.__file_name, 'r')  # Открываем файл для чтения
        content = file.read()  # Считываем все данные
        file.close()  # Закрываем файл
        return content

    def add(self, *products):
        existing_products = set()
        file = open(self.__file_name, 'r')
        for line in file:
            existing_products.add(line.strip().split(', ')[0].lower())  # Сохраняем названия в нижнем регистре
        file.close()
        # Запись новых продуктов
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name.lower() not in existing_products:
                file.write(f"{product}\n")
                print(f"Продукт добавлен: {product}")
            else:
                print(f"Продукт {product} уже есть в магазине")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Вывод продукта через __str__
s1.add(p1, p2, p3)  # Добавление продуктов
print(s1.get_products())  # Вывод всех продуктов
