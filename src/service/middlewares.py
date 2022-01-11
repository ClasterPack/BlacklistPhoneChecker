import logging
import time
from http import HTTPStatus

from aiohttp import web


@web.middleware
async def _log_request_data_middleware(request: web.Request, handler) -> web.StreamResponse:
    """Логирует информацию о запросе."""
    start_time = time.monotonic()
    response = await handler(request)
    logging.info({
        'time': time.monotonic() - start_time,
        'status_code': response.status,
        'request': {
            'method': request.method,
            'path': request.path,
            'headers': [
                '{pkey}: {pvalue}'.format(pkey=pkey, pvalue=pvalue)
                for pkey, pvalue in request.headers.items()
            ],
        },
    })
    return response


@web.middleware
async def _errors_middleware(request: web.Request, handler) -> web.StreamResponse:
    """Обрабатывает исключения."""
    try:
        http_response = await handler(request)
    except web.HTTPException as http_exc:
        http_response = web.json_response(
            {'error': http_exc.text},
            status=http_exc.status,
        )
    except Exception as exc:
        logging.exception('Unexpected error')
        http_response = web.json_response(
            {'error': str(exc)},
            status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
        )
    return http_response


def build_middlewares():
    """Создает мидлвари сервиса."""
    return (
        _log_request_data_middleware,
        _errors_middleware,
    )
