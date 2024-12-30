import allure
import requests
from utils.logger import Logger
"""Создание класса для отправки методов запроса"""
class Http_methods():
    headers = {"Conten-Type":"Application/json"}
    coockie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_requests(url, methods = "GET")
            result = requests.get(url, headers = Http_methods.headers, cookies = Http_methods.coockie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_requests(url, methods = "POST")
            result = requests.post(url, json = body, headers = Http_methods.headers, cookies = Http_methods.coockie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_requests(url, methods = "PUT")
            result = requests.put(url, json = body, headers = Http_methods.headers, cookies = Http_methods.coockie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_requests(url, methods = "DELETE")
            result = requests.delete(url, json = body, headers = Http_methods.headers, cookies = Http_methods.coockie)
            Logger.add_response(result)
            return result

