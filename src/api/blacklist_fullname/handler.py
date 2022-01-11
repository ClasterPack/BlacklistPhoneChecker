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


async def get_blacklist_fullnames(request: web.Request) -> web.Response:
    """Функция выдающая полный список имен пользователей состоящих в чёрном списке."""
    controller = request.app['fullname_blacklist']
    blacklist_response = BlacklistResponse(
        answer=controller.get_list(),
    )
    return web.json_response(BlacklistResponseSchema().dump(blacklist_response))


async def add_fullname_in_blacklist(request: web.Request) -> web.Response:
    """Функция внесения пользователя в черный список."""
    controller = request.app['fullname_blacklist']
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


async def update_fullname_in_blacklist(request: web.Request) -> web.Response:
    """Функция обновления срока давности пользователя в черном списке."""
    controller = request.app['fullname_blacklist']
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


async def check_fullname_in_blacklist(request: web.Request) -> web.Response:
    """Функция на вхождение пользователя в черный список."""
    controller = request.app['fullname_blacklist']

    blacklist_request: BlacklistRequest = await aiohttpparser.parser.parse(
        argmap=BlacklistRequestSchema,
        req=request,
        location='json',
    )
    blacklist_response = BlacklistFunctionResponse(
        function_answer=controller.check(blacklist_request.blacklist_data),
    )
    return web.json_response(BlacklistFunctionResponseSchema().dump(blacklist_response))


async def delete_fullname_from_blacklist(request: web.Request) -> web.Response:
    """Функция удаления пользователя из чёрного списка."""
    controller = request.app['fullname_blacklist']

    blacklist_request: BlacklistRequest = await aiohttpparser.parser.parse(
        argmap=BlacklistRequestSchema,
        req=request,
        location='json',
    )
    blacklist_response = BlacklistFunctionResponse(
        function_answer=controller.delete(blacklist_request.blacklist_data),
    )
    return web.json_response(BlacklistFunctionResponseSchema().dump(blacklist_response))
