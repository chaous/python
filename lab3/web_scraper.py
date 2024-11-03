import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    try:
        # Получаем HTML-данные с веб-сайта
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса
        
        # Парсим HTML-код
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Пример: Извлекаем заголовок страницы
        title = soup.title.string if soup.title else "Заголовок не найден"
        print(f"Заголовок страницы: {title}")
        
        # Пример: Извлекаем все ссылки на странице
        links = [a['href'] for a in soup.find_all('a', href=True)]
        print("Ссылки на странице:")
        for link in links:
            print(link)
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")

# URL для парсинга
url = "https://www.example.com"  # Замените на любой сайт для тестирования
fetch_and_parse(url)
