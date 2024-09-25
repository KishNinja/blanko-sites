# Сдесь есть курсы нужных для работы валют.
import requests

url = 'https://api.gemini.com/v2/ticker/btcusd'
response = requests.get(url)

# data = response.json()
print(response)