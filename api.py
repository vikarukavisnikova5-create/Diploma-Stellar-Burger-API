import allure
import requests
from data import REGISTER_URL, LOGIN_URL, USER_URL, INGREDIENTS_URL, ORDERS_URL

@allure.step('Регистрация пользователя')
def register_user(payload):
    return requests.post(REGISTER_URL, json=payload)

@allure.step('Логин пользователя')
def login_user(payload):
    return requests.post(LOGIN_URL, json=payload)

@allure.step('Удаление пользователя')
def delete_user(token):
    return requests.delete(USER_URL, headers={'Authorization': token})

@allure.step('Получение списка ингредиентов')
def get_ingredients():
    return requests.get(INGREDIENTS_URL)

@allure.step('Создание заказа')
def create_order(ingredients, token=None):
    headers = {'Authorization': token} if token else {}
    return requests.post(ORDERS_URL, json={'ingredients': ingredients}, headers=headers)