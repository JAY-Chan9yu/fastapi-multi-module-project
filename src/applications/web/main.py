from fastapi import FastAPI
from fastapi.middleware import Middleware

from container import MainContainer

from .api.main import router as main_router


def initialize_middlewares() -> list:
    from .middlewares.async_session_middleware import AsyncSessionMiddleware

    return [
        Middleware(AsyncSessionMiddleware),
    ]


def create_app():
    app = FastAPI(
        title="FastAPI",
        middleware=initialize_middlewares(),
    )
    app.container = MainContainer()
    app.include_router(main_router, prefix="")
    return app
