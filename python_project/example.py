from idlelib.iomenu import encoding
from textwrap import indent
import requests
import main

respone = requests.get('https://map.ukrainealarm.com/')

# Метод ok выводит True если статус кода не превышает от 200 до 399.
# Потому что 400 это ошибка пользователя, а 500 ошибка сервера.
def examination(s = respone.ok):
    if s:
        return f'Correct code - {s}'
    return f'Wrong code - {s}'

try:
    # В целом все начинают переходить на https запросы, ведь они намного безопасней чем http.
    respone_json = respone.json()
    with open('/Users/vlad/blanko-sites/python_project/date.json', 'w', encoding='utf-8') as file:
        # Записывать json в файл нужно только через метод dump.
        main.json.dump(respone_json, file, indent=2, ensure_ascii=False)
except:
    respone_text = respone.text
    with open('/Users/vlad/blanko-sites/index.html', 'w', encoding='utf-8') as file:
        # Записывать json в файл нужно только через метод dump.
        file.write(respone_text)