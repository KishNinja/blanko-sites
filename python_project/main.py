import json
import requests
'''
Типы (status_code)
1xx-Иформационные
2xx-Успешный
3xx-Перенаправленные
4xx-Клиентская ошибка
5xx-Ошибка сервера
'''

qu = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS57DltNK9zr13gCil9CR26p7ks3iVKut84MA&s')

try:
    with open('headers-photo.json', 'w', encoding='utf-8') as file:
        json.dump(dict(qu.headers), file, indent=2)
except:
    pass

try:
    with open('photo.jpeg', 'wb') as file:
        file.write(qu.content)
except:
    pass