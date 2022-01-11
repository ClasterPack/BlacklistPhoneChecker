import pytest
from pytest_mock import MockerFixture


async def test_get_list_from_blacklist(cli, mock_resp):
    resp = await cli.get('/phones')

    resp_json = await resp.json()
    assert resp_json == {'answer': [
        {'phone': '89993220000', 'expire_date': '2021-12-31'},
        {'phone': '89993220000', 'expire_date': '2022-5-9'},
        {'phone': '80554669500', 'expire_date': '2077-9-17'}
    ]}


async def test_failedfunc_from_blacklist(cli, mock_resp):
    resp = await cli.put('/phones/add', json={"blacklist_data": "89991267", "expire_date": "2022-5-5"})

    resp_json = await resp.json()
    assert resp_json == {'function_answer': False}


async def test_func_from_blacklist(cli, mock_resp):
    resp = await cli.put('/phones/add',
                         json={"blacklist_data": "89994500852", "expire_date": "2022-12-20"})

    resp_json = await resp.json()
    assert resp_json == {'function_answer': True}


async def test_wrong_http_method(cli, mock_resp):
    resp = await cli.get('/phones/add',
                         json={"blacklist_data": "89994500852", "expire_date": "2022-12-20"})

    resp_json = await resp.json()
    assert resp_json == {'error': '405: Method Not Allowed'}
