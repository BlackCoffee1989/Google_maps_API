"""Методы для проверки ответов запросов"""
import json

from requests import Response


class Checking():

    """Метод для проверки статус кода ответа на запрос"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"ПРОВАЛ!!! Статус код = {str(response.status_code)}"
        print(f"Успешно!!! Статус код = {str(response.status_code)}")

    """Метод проверки наличиния обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)         # Импортировали модуль json, метод loads() - импортирует строку в формат json
        assert list(token) == expected_value, f"ПРОВАЛ!!! Нужных полей нет"
        print(f"Все поля присутствуют")

    """Метод проверки значений наличиния обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"Зеначение '{str(expected_value)}' в поле '{str(field_name)}' не верное!!!"
        print(f"Значение '{str(expected_value)}' в поле '{str(field_name)}' верное!!!")

    """Метод проверки значений наличиния слова обязательном поле в ответе запроса"""

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f"Слово '{str(search_word)}' присутствует в поле '{str(field_name)}'")
        else:
            print(f"Слово '{str(search_word)}' не найдено в поле '{str(field_name)}'")