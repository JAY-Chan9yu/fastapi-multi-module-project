from pydantic import BaseModel, ConfigDict


class RetrieveUserResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str

    model_config = ConfigDict(from_attributes=True)


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str


class CreateUserResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str

    model_config = ConfigDict(from_attributes=True)
