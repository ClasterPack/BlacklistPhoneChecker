import aiohttp_cors
from aiohttp.web_app import Application

from src.api.blacklist_fullname.handler import (
    add_fullname_in_blacklist,
    check_fullname_in_blacklist,
    delete_fullname_from_blacklist,
    get_blacklist_fullnames,
    update_fullname_in_blacklist,
)
from src.api.blacklist_phone.handler import (
    add_phone_in_blacklist,
    check_phone_in_blacklist,
    delete_phone_from_blacklist,
    get_blacklist_phones,
    update_phones_in_blacklist,
)


def setup_routes(app: Application):
    """Настраивает эндпоинты сервиса с поддержкой CORS."""
    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers='*',
            allow_headers='*',
        ),
    })

    cors.add(app.router.add_get('/users', get_blacklist_fullnames))
    cors.add(app.router.add_get('/phones', get_blacklist_phones))

    cors.add(app.router.add_put('/users/add', add_fullname_in_blacklist))
    cors.add(app.router.add_put('/phones/add', add_phone_in_blacklist))

    cors.add(app.router.add_patch('/users/update', update_fullname_in_blacklist))
    cors.add(app.router.add_patch('/phones/update', update_phones_in_blacklist))

    cors.add(app.router.add_post('/users/check', check_fullname_in_blacklist))
    cors.add(app.router.add_post('/phones/check', check_phone_in_blacklist))

    cors.add(app.router.add_delete('/users/remove', delete_fullname_from_blacklist))
    cors.add(app.router.add_delete('/phones/remove', delete_phone_from_blacklist))
