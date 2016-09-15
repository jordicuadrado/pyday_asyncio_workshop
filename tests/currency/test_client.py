import pytest

from unittest import mock
from asynctest import MagicMock

from currency.client import CurrencyClient
from aiohttp.client_reqrep import ClientResponse

@pytest.fixture()
def build_aiohttp_client_response():
    async def build_response(content, status=200):
        cr = ClientResponse("get", "http://example.com")
        cr.status = status
        cr._content = content
        cr.headers = {"CONTENT-TYPE": "application/json"}
        cr._loop = MagicMock()
        return cr
    return build_response

class TestCurrencyClient:

    @pytest.fixture
    def response_service(self):
        return b'{"rates":{"USD":1.22}}'

    @pytest.mark.asyncio
    async def test_convert(self, build_aiohttp_client_response, response_service):
        with mock.patch('currency.client.ClientSession') as patched:
            patched.return_value.get.return_value = build_aiohttp_client_response(response_service)
            client = CurrencyClient()
            assert await client.convert('USD', 100) == 122
