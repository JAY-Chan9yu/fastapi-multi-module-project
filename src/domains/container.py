from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Container, Dependency

from domains.users.container import UserContainer


class DomainsContainer(DeclarativeContainer):
    config = Configuration()

    user_repository = Dependency()
    notification_push_api = Dependency()
    users = Container(
        UserContainer,
        config=config.users,
        user_repository=user_repository,
        notification_push_api=notification_push_api,
    )
