from typing import TYPE_CHECKING

from domains.users.user import User

if TYPE_CHECKING:
    from infra.rdb.users.user_repository import UserRepository


class UserCreator:
    def __init__(self, user_repository: "UserRepository"):
        self.user_repository = user_repository

    async def create_user(self, user: User) -> User:
        entity = await self.user_repository.create(**user.model_dump())
        return User.model_validate(entity)
