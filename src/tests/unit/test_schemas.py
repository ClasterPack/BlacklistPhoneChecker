import pytest
from marshmallow.exceptions import ValidationError

from src.api.schemas import BlacklistRequestSchema


def test_status_schema_ok(caplog):
    """Тест на сериализацию объекта входного запроса схемой."""
    request = {
        "blacklist_data": "New data",
        'expire_date': '2022-12-12',
    }
    BlacklistRequestSchema().load(request)
    assert not caplog.records


@pytest.mark.parametrize("request_data", [
    {"blacklist_data": 2255},
    {"blacklist_data": 2, "expire_date": 2019 - 8 - 8},
    {"bl"},
    {},
    {"expire_date": "2088-88-88"},
])
def test_status_witch_error(caplog, request_data):
    """Тест на сериализацию объекта входного запроса схемой."""
    with pytest.raises(ValidationError) as ex:
        BlacklistRequestSchema().load(request_data)
    assert not caplog.records
