import pytest

from src.api.controller import Blacklist


@pytest.mark.parametrize('blacklist_data, expire_data, answer', [
    ('Valera Petrov', '2022-2-5', True),
    ('88805553535', '2022-2-5', False),
    ('99', '99', False),
    ('99', '2022-9-9', False),
])
def test_blacklist_username_add(blacklist_data, expire_data, answer):
    """Проверка функции добавления ФИ в чёрный список."""
    bl_add = Blacklist('username').add(blacklist_data, expire_data)
    assert bl_add == answer


@pytest.mark.parametrize('blacklist_data, expire_data, answer', [
    ('89993220000', '2022-5-5', True),
    (88005553535, '2022-2-2', False),
    ('88005553535', '2050-2-2', True),
    ('Магомед Халилов', '2050-5-5', False),
    ('89999999999', '2019-5-5', False),
    ('899999999999', '2022-2-5', False),
])
def test_blacklist_phone_add(blacklist_data, expire_data, answer):
    """Проверка функции добавления телефона в чёрный список."""
    bl_add = Blacklist('phone').add(blacklist_data, expire_data)
    assert bl_add == answer
