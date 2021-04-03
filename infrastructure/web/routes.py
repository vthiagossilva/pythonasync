from starlette.routing import Route

from infrastructure.web.callbacks.create_user import create_user_callback

ROUTES = [
    Route("/auth/create/", create_user_callback, methods=["POST"])
]