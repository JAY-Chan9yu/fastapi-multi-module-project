from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Container, Singleton

from .engine import AsyncDatabase
from .users.container import UserContainer


class RelationalDatabaseContainer(DeclarativeContainer):
    config = Configuration()
    db = Singleton(
        AsyncDatabase,
        writer_url=config.writer_url,
        reader_url=config.reader_url,
        echo=config.echo,
    )
    users = Container(UserContainer, session=db.provided.session)
