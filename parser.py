import requests
import json

print('укажите URL(по дефолту простой пример json)')
url = input()
if url=='':
    url = "https://jsonplaceholder.typicode.com/posts"

try:

    response = requests.get(url)
    response.raise_for_status()


    data = response.json()


    with open("parsed.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Данные успешно сохранены в файл 'parsed.json'.")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе: {e}")
except json.JSONDecodeError:
    print("Ответ с сайта не является корректным JSON.")
