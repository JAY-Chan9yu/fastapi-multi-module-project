from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from infra.rdb.base.base_entity import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    first_name: Mapped[str] = mapped_column(String(250), nullable=False)
    last_name: Mapped[str] = mapped_column(String(250), nullable=False)
