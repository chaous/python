def read_file_with_numbers(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line.isdigit():  # Проверка, является ли строка числом
                    print(line)
                else:
                    raise TypeError(f"В строке '{line}' обнаружено значение, не являющееся числом.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except TypeError as e:
        print(f"Ошибка типа данных: {e}")

# Пример использования функции
read_file_with_numbers('data.txt')
