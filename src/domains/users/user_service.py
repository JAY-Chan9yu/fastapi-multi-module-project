from typing import TYPE_CHECKING
from uuid import uuid4

from .user import User
from .user_creator import UserCreator
from .user_reader import UserReader

if TYPE_CHECKING:
    from systems.notification_push_api.client import NotificationPushAPI


class UserService:
    def __init__(
        self,
        user_creator: UserCreator,
        user_reader: UserReader,
        notification_push_api: "NotificationPushAPI",
    ):
        self.user_creator = user_creator
        self.user_reader = user_reader
        self.notification_push_api = notification_push_api

    async def create_user(self, user: User) -> User:
        return await self.user_creator.create_user(user)

    async def get_user(self, user_id: int) -> User | None:
        return await self.user_reader.get_user(user_id)

    async def get_users(self, user_ids: list[int]) -> list[User]:
        return await self.user_reader.get_users(user_ids)

    async def send_user_created_notification(self, user: User) -> None:
        await self.notification_push_api.enqueue_push(message_id=uuid4.__str__(), payload=user.model_dump())
