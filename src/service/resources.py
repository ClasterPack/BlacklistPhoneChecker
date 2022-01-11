from aiohttp import web

from src.api.controller import Blacklist


async def setup_users_blacklist(app: web.Application):
    """Собирает класс с чёрным списком пользователей."""
    app['fullname_blacklist'] = Blacklist(key='username')


async def setup_phones_blacklist(app: web.Application):
    """Собирает класс с чёрным списком телефонов."""
    app['phones_blacklist'] = Blacklist(key='phone')
