from utils.Http_methods import Http_methods

base_url = "https://rahulshettyacademy.com"   # Базовый урл
key = "?key=qaclick123"                       # Обязательный параметр урл

"""Методы для тестирования Google_maps_api"""
class Google_maps_api():
    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():
        post_resource = "/maps/api/place/add/json"    # Ручка метода POST
        json_create_new_place = {                     # Тело запроса POST
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_url = base_url + post_resource + key     # Полный урл метода
        print(post_url)
        result_post = Http_methods.post(post_url, json_create_new_place)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"      # Ресурс к методу GET
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для обновления локации"""
    @staticmethod
    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json"   # Ресурс к методу PUT
        put_body = {                                   # Новое тело для обновления
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        put_url = base_url + put_resource + key
        print(put_url)
        result_put = Http_methods.put(put_url, put_body)
        print(result_put.text)
        return result_put

    """Метод для удаления новой локации"""
    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"    # Ресурс для метода DELETE
        delete_json = {                                    # Тело запроса DELETE
            "place_id": place_id
        }
        delete_url = base_url + delete_resource + key
        print(delete_url)
        result_delete = Http_methods.delete(delete_url, delete_json)
        print(result_delete.text)
        return result_delete

    @staticmethod
    def new_method():
        url = "https://dog.ceo/api/breed/hound/images"
        result_new = Http_methods.get(url)
        return result_new






