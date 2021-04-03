from starlette.applications import Starlette

from infrastructure.web.routes import ROUTES


app = Starlette(routes=ROUTES, debug=True)
