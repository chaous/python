import re
from collections import Counter

def count_unique_words(text):
    # Убираем знаки препинания и приводим текст к нижнему регистру
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Подсчитываем уникальные слова
    word_count = Counter(words)
    
    # Выводим количество уникальных слов
    unique_word_count = len(word_count)
    print(f"Количество уникальных слов: {unique_word_count}")
    return unique_word_count

# Пример использования
text = "Пример текста, который содержит несколько уникальных слов! Текст должен быть обработан."
count_unique_words(text)
