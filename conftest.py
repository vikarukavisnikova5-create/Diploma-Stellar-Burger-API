import pytest
from helpers import generate_user
from api import register_user, login_user, delete_user, get_ingredients

@pytest.fixture
def user_data():
    user = generate_user()
    yield user
    response = login_user({'email': user['email'], 'password': user['password']})
    if response.status_code == 200:
        delete_user(response.json()['accessToken'])

@pytest.fixture
def registered_user(user_data):
    response = register_user(user_data)
    return user_data, response.json()['accessToken']

@pytest.fixture
def ingredient_ids():
    data = get_ingredients().json()['data']
    return [data[0]['_id'], data[1]['_id']]