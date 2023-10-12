from typing import TYPE_CHECKING

from domains.users.user import User

if TYPE_CHECKING:
    from infra.rdb.users.user_repository import UserRepository


class UserReader:
    def __init__(self, user_repository: "UserRepository"):
        self.user_repository = user_repository

    async def get_user(self, user_id: int) -> User | None:
        if not (entity := await self.user_repository.get_by_id_or_none(user_id)):
            return None
        return User.model_validate(entity)

    async def get_users(self, user_ids: list[int]) -> list[User]:
        entities = await self.user_repository.find_by_ids(user_ids)
        return [User.model_validate(entity) for entity in entities]
