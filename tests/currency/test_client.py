import pytest

from unittest import mock

from currency.client import CurrencyClient

class TestCurrencyClient:

    @pytest.fixture
    def response_service(self):
        raise NotImplementedError

    @pytest.mark.asyncio
    async def test_convert(self, build_aiohttp_client_response, response_service):
        with mock.patch('currency.client.ClientSession') as patched:
            patched.return_value.get.return_value = build_aiohttp_client_response(response_service)
            raise NotImplementedError
