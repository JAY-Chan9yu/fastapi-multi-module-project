from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Dependency, Factory

from infra.rdb.users.user_repository import UserRepository


class UserContainer(DeclarativeContainer):
    session = Dependency()
    user_repository = Factory(UserRepository, session=session)
