import binascii

from aiohttp import web
from aiohttp.web_exceptions import HTTPNotFound

from currency_sync.client import CurrencyClient


async def convert(request):
    try:
        currency = request.match_info['currency']
        amount = request.match_info['amount']
    except KeyError:
        return HTTPNotFound()

    client = CurrencyClient()
    amount_converted = await client.convert(currency, int(amount))
    return web.Response(body=binascii.a2b_qp("{} {}".format(currency, str(amount_converted))))


def build_app(*args, **kwargs):
    app = web.Application()
    app.router.add_route('GET', '/convert/{currency}/{amount}', convert)
    return app


if __name__ == '__main__':
    app = build_app()
    web.run_app(app)
