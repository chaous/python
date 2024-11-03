import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", handlers=[logging.FileHandler("warehouse_log.txt"), logging.StreamHandler()])

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def increase_quantity(self, amount):
        self.quantity += amount
        logging.info(f"Увеличено количество товара '{self.name}' на {amount}. Текущее количество: {self.quantity}")
    
    def decrease_quantity(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            logging.info(f"Уменьшено количество товара '{self.name}' на {amount}. Текущее количество: {self.quantity}")
        else:
            raise ValueError(f"Недостаточно товара '{self.name}' для уменьшения на {amount}")
    
    def calculate_total_price(self):
        return self.quantity * self.price

class Warehouse:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        logging.info(f"Товар '{product.name}' добавлен на склад. Количество: {product.quantity}, Цена: {product.price}")
    
    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]
        logging.info(f"Товар '{product_name}' удален со склада.")
    
    def calculate_total_value(self):
        total = sum(product.calculate_total_price() for product in self.products)
        logging.info(f"Рассчитана общая стоимость товаров на складе: {total}")
        return total

class Seller:
    def __init__(self, name):
        self.name = name
        self.sales_report = []

    def sell_product(self, warehouse, product_name, quantity):
        for product in warehouse.products:
            if product.name == product_name:
                if quantity > product.quantity:
                    raise ValueError(f"Недостаточно товара '{product.name}' для продажи {quantity} единиц.")
                product.decrease_quantity(quantity)
                revenue = quantity * product.price
                self.sales_report.append({"product": product.name, "quantity": quantity, "revenue": revenue})
                logging.info(f"Продавец {self.name} продал {quantity} единиц товара '{product.name}' на сумму {revenue}")
                return
        raise ValueError(f"Товар '{product_name}' не найден на складе.")
    
    def sales_report_summary(self):
        for sale in self.sales_report:
            print(f"Товар: {sale['product']}, Количество: {sale['quantity']}, Выручка: {sale['revenue']}")
        total_revenue = sum(sale["revenue"] for sale in self.sales_report)
        print(f"Общая выручка: {total_revenue}")
        logging.info(f"Продавец {self.name} сформировал отчёт о продажах. Общая выручка: {total_revenue}")

# Пример использования программы
warehouse = Warehouse()
seller = Seller("Иван")

# Добавление товаров на склад
product1 = Product("Ноутбук", 10, 50000)
product2 = Product("Телефон", 20, 30000)
warehouse.add_product(product1)
warehouse.add_product(product2)

# Продажа товаров
seller.sell_product(warehouse, "Ноутбук", 2)
seller.sell_product(warehouse, "Телефон", 5)

# Формирование отчета о продажах
seller.sales_report_summary()

# Расчет общей стоимости товаров на складе
warehouse.calculate_total_value()
