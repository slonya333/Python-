import pytest
import requests
from jsonschema import validate
import time

# Добавим задержки между запросами, чтобы избежать проблем с лимитами API
API_DELAY = 0.5  # 500ms между запросами
import requests
from jsonschema import validate

# Тест для получения списка пользователей с проверкой статус-кода и наличия поля "data"
def test_get_users():  
    response = requests.get("https://reqres.in/api/users?page=2")  
    assert response.status_code == 200  
    data = response.json()  
    assert "data" in data

# Схема для валидации ответа
schema = {  
    "type": "object",  
    "properties": {  
        "page": {"type": "number"},  
        "per_page": {"type": "number"},
        "total": {"type": "number"},
        "total_pages": {"type": "number"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string"}
                },
                "required": ["id", "email", "first_name", "last_name", "avatar"]
            }
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "text": {"type": "string"}
            },
            "required": ["url", "text"]
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data", "support"]
}

# Тест для проверки схемы ответа
def test_get_users_schema():  
    response = requests.get("https://reqres.in/api/users?page=2")  
    assert response.status_code == 200
    assert validate(instance=response.json(), schema=schema) is None
    import requests
import pytest
from jsonschema import validate
# Схема для проверки ответа
CREATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "job": {"type": "string"},},
    "required": ["id"]}
def test_create_user():
    payload = {"name": "Alice", "job": "Engineer"}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=payload)
    assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
    response_data = response.json()
    # Проверка схемы и типа ID
    validate(instance=response_data, schema=CREATE_USER_SCHEMA)
    assert isinstance(response_data["id"], int), "ID должен быть целым числом"
    assert response_data["id"] > 0, "ID должен быть положительным числом"
@pytest.mark.parametrize("name, job", [
    ("Bob", "QA Engineer"),
    ("Eve", "DevOps Specialist"),
    ("Mike", "Product Manager"),
    ("Sarah", "UX Designer")])
def test_create_user_params(name, job):
    payload = {"name": name, "job": job}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=payload)
    assert response.status_code == 201
    response_data = response.json()
    # Проверки для параметризованных тестов
    assert isinstance(response_data["id"], int), f"ID должен быть int, получен {type(response_data['id'])}"
    assert response_data["id"] > 0, f"ID {response_data['id']} не является положительным числом"
import requests
def test_invalid_login():
    """Тест неверного запроса с ожидаемым кодом 400"""
    response = requests.post(
        "https://httpbin.org/status/400",
        json={"email": "invalid_email"} )
    assert response.status_code == 400, f"Ожидался статус 400 (Bad Request), получен {response.status_code}"
def test_not_found():
    """Тест несуществующего ресурса с ожидаемым кодом 404"""
    response = requests.get("https://httpbin.org/status/404")
    assert response.status_code == 404, f"Ожидался статус 404 (Not Found), получен {response.status_code}"
