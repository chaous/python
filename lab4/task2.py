import itertools

# Задача 1: Создание бесконечного генератора чисел
infinite_counter = itertools.count(start=1, step=1)
print("Первые 5 чисел из бесконечного генератора:")
for _ in range(5):
    print(next(infinite_counter))

# Задача 2: Применение функции к каждому элементу в итераторе
numbers = [1, 2, 3, 4, 5]
squared_numbers = itertools.starmap(lambda x: x**2, [(n,) for n in numbers])
print("\nКвадраты чисел из списка:", list(squared_numbers))

# Задача 3: Объединение нескольких итераторов в один
iter1 = [1, 2, 3]
iter2 = ['a', 'b', 'c']
iter3 = [10.5, 20.5, 30.5]

combined_iterator = itertools.chain(iter1, iter2, iter3)
print("\nОбъединённый итератор:")
for item in combined_iterator:
    print(item)

# Обработка исключений при отсутствии данных
try:
    empty_iterator = iter([])
    first_item = next(empty_iterator)
    print(f"\nПервый элемент из пустого итератора: {first_item}")
except StopIteration:
    print("\nИсключение StopIteration: Итератор пуст и не содержит данных.")
