import httpx
from starlette.datastructures import MutableHeaders


TIMEOUT = 45  # TODO: env vars


async def send_request(url, body, headers: MutableHeaders, method) -> str:
    async with httpx.AsyncClient() as client:
        return await getattr(client, method)(
            url,
            headers=headers,
            json=body,
            timeout=TIMEOUT,
        )
