import pytest

from src.api.controller import Blacklist


@pytest.mark.parametrize('blacklist_data, new_expire_date, answer', [
    ('89993220000', '2055-5-5', True),
    (88005553535, '2025-5-5', False),
    ('88005553535', '2025-5-5', True),
    ('Магомед Халилов', '2019-5-5', False),
    ('88005553535', '2019-5-5', True),
])
def test_blacklist_update_phones(blacklist_data, new_expire_date, answer):
    """Проверка обновления в черном списке."""
    bl_upd = Blacklist('phone').update(blacklist_data, new_expire_date)
    assert bl_upd == answer


@pytest.mark.parametrize('blacklist_data, new_expire_date, answer', [
    ('89993220000', '2055-5-5', False),
    ('Магомед Халилов', '2019-5-5', True),
    ('Маго2 Халилов', '2019-5-5', False),
    (49849848, '2025-5-5', False),
])
def test_blacklist_update_fullname(blacklist_data, new_expire_date, answer):
    """Проверка обновления в черном списке."""
    bl_upd = Blacklist('username').update(blacklist_data, new_expire_date)
    assert bl_upd == answer
