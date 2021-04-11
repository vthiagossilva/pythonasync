from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from application.users.use_cases.create_user.use_case import create_user_uc


async def create_user_callback(request: Request):
    try:
        data = await request.json()
    except ValueError:
        return Response("Um JSON era esperado", 400)

    result, code = await create_user_uc(data)

    return Response(result, status_code=code)
