from domains.base.model import Model


class User(Model):
    id: int | None = None
    username: str
    email: str
    first_name: str
    last_name: str
