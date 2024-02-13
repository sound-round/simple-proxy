from fastapi import FastAPI, Request
from fastapi import HTTPException
from starlette.datastructures import MutableHeaders
from httpx import HTTPStatusError

from .client import send_request


app = FastAPI()

@app.get("/")
async def get_root():
    return {"status": True}


# TODO: make other methods work
@app.api_route("/request", methods=["POST"])
async def process_request(request: Request):
    try:
        body: dict = await request.json()
        url = body.pop("url")  # get url from body and remove it from body
    except ValueError:
        raise HTTPException(status_code=400, detail="Bad request")
    except KeyError:
        raise HTTPException(status_code=400, detail="url is required")
    headers = MutableHeaders(request.headers)
    del headers["content-length"]
    method = request.method.lower()

    try:
        response = await send_request(url, body, headers, method)
        status_code = response.status_code
        response.raise_for_status()
        return response.json()

    except HTTPStatusError as exc:
        raise HTTPException(status_code=status_code, detail=str(exc))
