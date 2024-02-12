import pytest
from unittest import mock
from httpx import Response, Request


@pytest.fixture()
def response():
    def fabric(status_code=200, request=None, **kwargs):
        if request is None:
            request = Request("GET", "/")
        return Response(status_code, request=request, **kwargs)

    return fabric


@pytest.fixture()
def httpx(response):
    with mock.patch("httpx.AsyncClient.send") as mocked:
        mocked.return_value = response(json={})
        yield mocked
