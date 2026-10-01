import uuid

def generate_user():
    suffix = uuid.uuid4().hex[:8]
    return {
        'email': f'test_{suffix}@yandex.ru',
        'password': f'pass_{suffix}',
        'name': f'User{suffix}',
    }