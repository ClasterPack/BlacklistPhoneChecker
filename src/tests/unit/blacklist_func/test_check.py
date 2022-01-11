import pytest

from src.api.controller import Blacklist


@pytest.mark.parametrize('blacklist_data, answer', [
    ('80554669500', True),
    ('88005553535', False),
    ('89993220000', True),
    ('Магомед Халилов', False),
])
def test_blacklist_check_phones(blacklist_data, answer):
    """Проверка функции поиска телефона в черном списке."""
    bl_check = Blacklist('phone').check(blacklist_data)
    assert bl_check == answer


@pytest.mark.parametrize('blacklist_data, answer', [
    ('Магомед Халилов', True),
    ('Николай Ридтц', False),
    ('Денис Шарипов', True),
    ('880005553535', False),
])
def test_blacklist_check_names(blacklist_data, answer):
    """Проверка функции поиска ФИ в черном списке."""
    bl_check = Blacklist('username').check(blacklist_data)
    assert bl_check == answer
