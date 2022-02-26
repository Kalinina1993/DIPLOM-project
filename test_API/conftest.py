import pytest
import requests
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")


@pytest.fixture(scope="class")
def new_user():
    response = requests.post("https://petstore.swagger.io/v2/user", json={"id": 0,
                                                                          "username": "Kalina",
                                                                          "firstName": "Natasha",
                                                                          "lastName": "Kalinina",
                                                                          "email": "www.kalina@mail.ru",
                                                                          "password": "8888",
                                                                          "phone": "01",
                                                                          "userStatus": "0"})
    return response


@pytest.fixture(scope="class")
def user_datas():
    """User datas for login"""
    response = requests.get("https://petstore.swagger.io/v2/user/login?username=Kalina&password=8888",
                            json={"username": "Kalinkina",
                                  "password": "8888"})
    return response


@pytest.fixture(scope="class")
def user_username():
    response = requests.get("https://petstore.swagger.io/v2/user/Kalina")
    return response


@pytest.fixture(scope="class")
def delete_user():
    """User datas for delete"""
    response = requests.delete("https://petstore.swagger.io/v2/user/Kalina")
    return response


@pytest.fixture(scope="class")
def adding_pet():
    """Pet datas for adding"""
    response = requests.post("https://petstore.swagger.io/v2/pet",
                             json={
                                 "id": 8,
                                 "category": {
                                     "id": 8,
                                     "name": "cat"
                                 },
                                 "name": "Marik",
                                 "photoUrls": [
                                     "url"
                                 ],
                                 "tags": [
                                     {
                                         "id": 8,
                                         "name": "Marik"
                                     }
                                 ],
                                 "status": "available"
                             })
    return response


@pytest.fixture(scope="class")
def update_name_pet():
    """Pet datas for adding"""
    response = requests.put("https://petstore.swagger.io/v2/pet",
                            json={
                                "id": 8,
                                "category": {
                                    "id": 8,
                                    "name": "cat"
                                },
                                "name": "Orange",
                                "photoUrls": [
                                    "url"
                                ],
                                "tags": [
                                    {
                                        "id": 8,
                                        "name": "Orange"
                                    }
                                ],
                                "status": "available"
                            })
    return response
