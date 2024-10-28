"""Получение информации через API, парсинг и сохранение в БД"""

from pprint import pprint
import requests
import yaml


# Временное решение получение токена. Далее будет тянуться из БД
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

TOKEN = config["TOKEN"]
headers = {"key": TOKEN}

URL = "http://api.weatherapi.com/v1/current.json?q=Moscow&aqi=yes"

try:
    response = requests.post(URL, headers=headers, timeout=20)
    response.raise_for_status()
    data = response.json()
    pprint(data)
except requests.exceptions.Timeout:
    print("Запрос превысил время ожидания")
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка: {e}")

# Переделать функцию под текущие реалии
def get_info_about_weather(answer: dict) -> dict:
    """
    Парсинг полученного словаря
    для получение текущей погоды
    """

    for key, value in answer.items():
        if key == "now":
            return value

        result = get_info_about_weather(value)

        if result is not None:
            return result

    raise KeyError("Ключ 'now' отсутствует")
