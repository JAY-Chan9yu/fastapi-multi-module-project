from unittest.mock import Mock

import pytest

from domains.users.user import User
from domains.users.user_creator import UserCreator
from domains.users.user_service import UserService


class TestUserService:
    sut: UserService

    @pytest.mark.asyncio
    async def test_create_user(self, container):
        user_creator = Mock(spec=UserCreator)
        user_creator.create_user.return_value = (
            expected := User(
                id=1,
                username="tester-name",
                email="test-email@email.com",
                first_name="test-first-name",
                last_name="test-last-name",
            )
        )
        with container.domains().users().user_creator.override(user_creator):
            user_service = container.domains().users().user_service()
            result = await user_service.create_user(
                user=User(
                    username="tester-name",
                    email="test-email@email.com",
                    first_name="test-first-name",
                    last_name="test-last-name",
                )
            )
        assert expected.id == result.id
        assert expected.username == result.username
        assert expected.email == result.email
        assert expected.first_name == result.first_name
        assert expected.last_name == result.last_name
