import pytest


@pytest.fixture
def good_resp_from_blacklist_operation():
    return {'function_answer': True}


@pytest.fixture
def good_resp_from_get_blacklist():
    return {
        [
                {'username': 'Виталий Волочай', 'expire_date': '2021-12-1'},
                {'username': 'Денис Шарипов', 'expire_date': '2022-5-9'},
                {'username': 'Николай Ридтц', 'expire_date': '2007-7-5'},
                {'username': 'Магомед Халилов', 'expire_date': '2142-2-23'}
        ]
    }
