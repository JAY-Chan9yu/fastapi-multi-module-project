from typing import Generic, Sequence, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import async_scoped_session

from infra.rdb.base.base_entity import BaseEntity

T = TypeVar("T", bound=BaseEntity)


class BaseRepository(Generic[T]):
    entity: Type[T]
    session: async_scoped_session

    def __init__(self, entity: Type[T], session: async_scoped_session):
        self.entity = entity
        self.session = session

    @property
    def table(self):
        return BaseEntity.metadata.tables[self.entity.__tablename__]

    async def create(self, **kwargs) -> T:
        self.session.add(entity := self.entity(**kwargs))
        try:
            await self.session.flush()
        except IntegrityError as e:
            await self.session.rollback()
            raise e
        return entity

    async def get_by_id_or_none(self, id: int) -> T | None:
        stmt = select(self.entity).where(self.entity.id == id)
        result = await self.session.execute(stmt)
        entity = result.scalars().first()
        return entity

    async def find_by_ids(self, ids: list[int]) -> Sequence[T]:
        stmt = select(self.entity).where(self.entity.id.in_(ids))
        result = await self.session.execute(stmt)
        entities = result.scalars().all()
        return entities
