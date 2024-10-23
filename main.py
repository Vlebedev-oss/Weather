import pprint
import requests
import yaml


# Временное решение получение токена. Далее будет тянуться из БД
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

TOKEN = config["TOKEN"]
URL = f"https://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID={TOKEN}"

try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    pprint.pprint(data)
except requests.exceptions.Timeout:
    print("Запрос превысил время ожидания")
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка: {e}")
