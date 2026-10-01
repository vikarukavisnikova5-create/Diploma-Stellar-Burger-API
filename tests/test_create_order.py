import allure
from api import create_order
from data import NO_INGREDIENTS

@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_with_auth_and_ingredients_success(self, registered_user, ingredient_ids):
        _, token = registered_user
        response = create_order(ingredient_ids, token)
        assert response.status_code == 200
        assert 'number' in response.json()['order']

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth_success(self, ingredient_ids):
        response = create_order(ingredient_ids)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients_error(self, registered_user):
        _, token = registered_user
        response = create_order([], token)
        assert response.status_code == 400
        assert response.json()['message'] == NO_INGREDIENTS

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_hash_error(self, registered_user):
        _, token = registered_user
        response = create_order(['invalid_hash_123'], token)
        assert response.status_code == 500