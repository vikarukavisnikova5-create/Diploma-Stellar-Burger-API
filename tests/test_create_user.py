import allure
import pytest
from api import register_user
from data import USER_EXISTS, REQUIRED_FIELDS

@allure.feature('Создание пользователя')
class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user_success(self, user_data):
        response = register_user(user_data)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Нельзя создать пользователя, который уже зарегистрирован')
    def test_create_existing_user_error(self, registered_user):
        user, _ = registered_user
        response = register_user(user)
        assert response.status_code == 403
        assert response.json()['message'] == USER_EXISTS

    @allure.title('Нельзя создать пользователя без обязательного поля')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_without_required_field_error(self, user_data, field):
        payload = dict(user_data)
        del payload[field]
        response = register_user(payload)
        assert response.status_code == 403
        assert response.json()['message'] == REQUIRED_FIELDS