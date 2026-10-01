import allure
import pytest
from api import login_user
from data import INCORRECT_LOGIN

@allure.feature('Логин пользователя')
class TestLogin:

    @allure.title('Вход под существующим пользователем')
    def test_login_existing_user_success(self, registered_user):
        user, _ = registered_user
        response = login_user({'email': user['email'], 'password': user['password']})
        assert response.status_code == 200
        assert 'accessToken' in response.json()

    @allure.title('Вход с неверным логином или паролем')
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_login_with_wrong_credentials_error(self, registered_user, field):
        user, _ = registered_user
        payload = {'email': user['email'], 'password': user['password']}
        payload[field] = 'wrong_' + payload[field]
        response = login_user(payload)
        assert response.status_code == 401
        assert response.json()['message'] == INCORRECT_LOGIN