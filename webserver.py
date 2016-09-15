import binascii

from aiohttp import web
from aiohttp.web_exceptions import HTTPNotFound

from currency.client import CurrencyClient


async def convert(request):
    try:
        currency = request.match_info['currency']
        amount = request.match_info['amount']
    except KeyError:
        return HTTPNotFound()

    raise NotImplementedError


def build_app(*args, **kwargs):
    app = web.Application()
    app.router.add_route('GET', '/convert/{currency}/{amount}', convert)
    return app


if __name__ == '__main__':
    app = build_app()
    web.run_app(app)
