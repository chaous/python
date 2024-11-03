class DataBuffer:
    def __init__(self):
        self.buffer = []

    def add_data(self, data):
        if len(self.buffer) >= 5:
            print("Переполнение буфера. Очистка буфера.")
            self.buffer.clear()
        self.buffer.append(data)
        print(f"Данные '{data}' добавлены в буфер.")

    def get_data(self):
        if not self.buffer:
            print("Буфер пуст. Нет данных для получения.")
        else:
            data = self.buffer.pop(0)
            print(f"Получены данные из буфера: {data}")
            return data

# Пример использования
buffer = DataBuffer()

# Добавление данных в буфер
buffer.add_data(1)
buffer.add_data(2)
buffer.add_data(3)
buffer.add_data(4)
buffer.add_data(5)
buffer.add_data(6)  # Это вызовет переполнение буфера и очистку

# Получение данных из буфера
buffer.get_data()
buffer.get_data()
buffer.get_data()
buffer.get_data()
buffer.get_data()  # Буфер будет пуст после этого вызова
buffer.get_data()  # Сообщение об отсутствии данных
