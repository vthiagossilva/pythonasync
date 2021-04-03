from starlette.requests import Request
from starlette.responses import JSONResponse


async def create_user_callback(request: Request):
    return JSONResponse({"response": "success"})
