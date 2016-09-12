import pytest

from asynctest import MagicMock

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
