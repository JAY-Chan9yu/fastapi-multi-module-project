from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, status
from fastapi.background import BackgroundTasks

from applications.web.api.v1.users.schemas import CreateUserRequest, CreateUserResponse, RetrieveUserResponse
from domains.users.user import User

router = APIRouter()


@router.get(
    "/{user_id}",
    responses={200: {"model": RetrieveUserResponse}},
    description="Retrieve user by id.",
)
@inject
async def get_user(
    user_id: int,
    user_service=Depends(Provide["domains.users.user_service"]),
):
    user = await user_service.get_user(user_id)
    return RetrieveUserResponse.model_validate(user)


@router.post(
    "/",
    responses={201: {"model": CreateUserResponse}},
    status_code=status.HTTP_201_CREATED,
    description="Create user.",
)
@inject
async def create_user(
    request: CreateUserRequest,
    background_tasks: BackgroundTasks,
    user_service=Depends(Provide["domains.users.user_service"]),
):
    user = await user_service.create_user(User.model_validate(request))
    background_tasks.add_task(user_service.send_user_created_notification, user=user)
    return CreateUserResponse.model_validate(user)
