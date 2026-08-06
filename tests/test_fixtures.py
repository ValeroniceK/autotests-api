import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print('[AUTOUSE] Отправляем данные в сервис аналитики')

@pytest.fixture(scope='session')
def settings():
    print('[SESSION] Инициализируем настройки автоетстов')

@pytest.fixture(scope='class')
def user():
    print('[CLASS] Создаем данные пользователя один раз на тестовый класс')

@pytest.fixture(scope='function')
def users_client():
    print('[FUNCTION] Создать API client на каждый автотес')


class TestUserFlow:
    def test_user_can_login(self,settings, user, users_client):
        ...

    def test_user_can_create_course(self,settings, user, users_client):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        ...



@pytest.fixture
def user_data() -> dict:
    return {'username': 'user_name', 'email': 'test@example.com'}

def test_user_email(user_data: dict):
    print(user_data)
    assert user_data['email'] == 'test@example.com'

def test_user_name(user_data: dict):
    print(user_data)
    assert user_data['username'] == 'user_name'



@pytest.fixture
def user_data_2() -> dict:
    print('Создаем пользователя до теста (setup)')
    yield {'username': 'user_name', 'email': 'test@example.com'}
    print('Удаляем пользователя после теста (teardown)')

def test_user_email_2(user_data_2: dict):
    print(user_data_2)
    assert user_data_2['email'] == 'test@example.com'
