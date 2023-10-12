from typing import TYPE_CHECKING

from infra.rdb.base.base_repository import BaseRepository
from infra.rdb.users.user_entity import UserEntity

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import async_scoped_session


class UserRepository(BaseRepository[UserEntity]):
    def __init__(self, session: "async_scoped_session"):
        super().__init__(UserEntity, session)
