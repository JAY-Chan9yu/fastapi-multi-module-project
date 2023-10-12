from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Dependency, Factory

from .user_creator import UserCreator
from .user_reader import UserReader
from .user_service import UserService


class UserContainer(DeclarativeContainer):
    config = Configuration()
    user_repository = Dependency()
    notification_push_api = Dependency()

    user_reader = Factory(UserReader, user_repository=user_repository)
    user_creator = Factory(UserCreator, user_repository=user_repository)
    user_service = Factory(
        UserService,
        user_creator=user_creator,
        user_reader=user_reader,
        notification_push_api=notification_push_api,
    )
