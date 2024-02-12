from fastapi import FastAPI, Request

from .client import send_request


app = FastAPI()

@app.get("/")
async def get_root():
    return {"status": True}


@app.post("/request")
async def process_request(request: Request):
    body: dict = await request.json()
    url = body.pop("url")  # get url from body and remove it from body
    headers = request.headers
    method = request.method.lower()
    return await send_request(url, body, headers, method)
