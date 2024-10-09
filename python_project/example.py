import requests
import main

respone = requests.get('https://api.github.com')
print(respone.status_code)

# Метод Ok выводит True если статус код меньше 400.
# print(respone.ok)

def verifyti(arg):
    if arg.ok:
        return f'{arg.status_code}'
    return False

print(verifyti(respone))

# метод text дает ответ сервера инит кода в виде строки.
# print(respone.file)

# Метод content используется больше для работы с файлами.
# Сам по себе метод content выдает ответ в байтах.
# print(respone.content)

respone_json = respone.json()

if main.os.path.isfile('python_project/date.json'):
    main.os.remove('python_project/date.json')
    # with open('python_project/')
