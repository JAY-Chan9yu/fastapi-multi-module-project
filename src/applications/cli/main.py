import typer

from applications.cli.base import AsyncTyper
from container import MainContainer


def create_app() -> AsyncTyper:
    app = AsyncTyper()
    container = MainContainer()

    @app.command()
    def foo():
        typer.echo("foo")

    @app.async_command()
    async def bar():
        db = container.infra().rdb().db()
        await db.create_all()

    return app
