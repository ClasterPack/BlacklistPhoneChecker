from aiohttp import web
from webargs import aiohttpparser

from src.api.schemas import (
    BlacklistFunctionResponse,
    BlacklistFunctionResponseSchema,
    BlacklistRequest,
    BlacklistRequestSchema,
    BlacklistResponse,
    BlacklistResponseSchema,
)


async def get_blacklist_phones(request: web.Request) -> web.Response:
    """Функция выдающая полный список телефонных номеров пользователей состоящих в чёрном списке."""
    controller = request.app['phones_blacklist']
    blacklist_response = BlacklistResponse(
        answer=controller.get_list(),
    )
    return web.json_response(BlacklistResponseSchema().dump(blacklist_response))


async def add_phone_in_blacklist(request: web.Request) -> web.Response:
    """Функция внесения телефона в черный список."""
    controller = request.app['phones_blacklist']
    blacklist_request: BlacklistRequest = await aiohttpparser.parser.parse(
        argmap=BlacklistRequestSchema,
        req=request,
        location='json',
    )
    blacklist_response = BlacklistFunctionResponse(
        function_answer=controller.add(
            blacklist_request.blacklist_data, blacklist_request.expire_date,
        ),
    )
    return web.json_response(BlacklistFunctionResponseSchema().dump(blacklist_response))


async def update_phones_in_blacklist(request: web.Request) -> web.Response:
    """Функция обновления срока давности по номеру телефона в черном списке."""
    controller = request.app['phones_blacklist']

    blacklist_request: BlacklistRequest = await aiohttpparser.parser.parse(
        argmap=BlacklistRequestSchema,
        req=request,
        location='json',
    )
    blacklist_response = BlacklistFunctionResponse(
        function_answer=controller.update(
            blacklist_request.blacklist_data, blacklist_request.expire_date,
        ),
    )
    return web.json_response(BlacklistFunctionResponseSchema().dump(blacklist_response))


async def check_phone_in_blacklist(request: web.Request) -> web.Response:
    """Функция на вхождение телефона в черный список."""
    controller = request.app['phones_blacklist']

    blacklist_request: BlacklistRequest = await aiohttpparser.parser.parse(
        argmap=BlacklistRequestSchema,
        req=request,
        location='json',
    )
    blacklist_response = BlacklistFunctionResponse(
        function_answer=controller.check(blacklist_request.blacklist_data),
    )
    return web.json_response(BlacklistFunctionResponseSchema().dump(blacklist_response))


async def delete_phone_from_blacklist(request: web.Request) -> web.Response:
    """Функция удаления телефонного номера из чёрного списка."""
    controller = request.app['phones_blacklist']

    blacklist_request: BlacklistRequest = await aiohttpparser.parser.parse(
        argmap=BlacklistRequestSchema,
        req=request,
        location='json',
    )
    blacklist_response = BlacklistFunctionResponse(
        function_answer=controller.delete(blacklist_request.blacklist_data),
    )
    return web.json_response(BlacklistFunctionResponseSchema().dump(blacklist_response))
