from datetime import datetime, timedelta

# Задача 1: Отображение текущей даты и времени
current_datetime = datetime.now()
print("Текущая дата и время:", current_datetime)

# Задача 2: Вычисление разницы между двумя датами
date1 = datetime(2023, 10, 25)
date2 = datetime(2024, 11, 3)
date_difference = date2 - date1
print("Разница между двумя датами:", date_difference.days, "дней")

# Задача 3: Преобразование строки в объект даты и времени
date_string = "2024-11-03 15:30:00"
date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Преобразованная строка в объект даты и времени:", date_object)

# Дополнительный пример: добавление дней к дате
days_to_add = 7
new_date = current_datetime + timedelta(days=days_to_add)
print(f"Дата через {days_to_add} дней:", new_date)
