from dependency_injector.wiring import inject, Provide
from starlette.types import ASGIApp, Receive, Scope, Send


@inject
def get_async_scoped_session(session=Provide["infra.rdb.db.provided.session"]):
    return session


class AsyncSessionMiddleware:
    """
    https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#using-asyncio-scoped-session
    Using current_task() for the “key” in the scope requires that
    the async_scoped_session.remove() method is called from within the outermost awaitable,
    to ensure the key is removed from the registry when the task is complete,
    otherwise the task handle as well as the AsyncSession will remain in memory,
    essentially creating a memory leak.
    """

    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        session = get_async_scoped_session()
        try:
            await self.app(scope, receive, send)
        except Exception as e:
            raise e
        else:
            await session.commit()
        finally:
            await session.remove()
