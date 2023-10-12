from datetime import datetime, timezone

from sqlalchemy.orm import Mapped, mapped_column

from infra.rdb.base.base import Base
from infra.rdb.fields import AwareDatetime


def tz_aware_utc_now():
    return datetime.now(timezone.utc)


class BaseEntity(Base):
    __abstract__ = True
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_charset": "utf8mb4"}

    created_at: Mapped[datetime] = mapped_column(AwareDatetime, nullable=False, default=tz_aware_utc_now)
    updated_at: Mapped[datetime] = mapped_column(
        AwareDatetime,
        nullable=False,
        default=tz_aware_utc_now,
        onupdate=tz_aware_utc_now,
    )
    deleted_at: Mapped[datetime | None] = mapped_column(AwareDatetime, nullable=True, default=None)
    is_deleted: Mapped[bool] = mapped_column(nullable=False, default=False, server_default="0")
