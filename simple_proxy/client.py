import httpx


TIMEOUT = 45  # TODO: env vars


async def send_request(url, body, headers, method) -> str:
    async with httpx.AsyncClient() as client:
        response = await getattr(client, method)(
            url,
            headers=headers,
            json=body,
            timeout=TIMEOUT,
        )

        response.raise_for_status()
        return response.json()
