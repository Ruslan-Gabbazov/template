from typing import Sequence

from sqlalchemy import select

from db.models.item import Item
from db.repository.base import BaseDatabaseRepository


class ItemRepository(BaseDatabaseRepository):
    async def get_items(self) -> Sequence[Item]:
        query_result = await self._session.execute(select(Item))

        return query_result.scalars().all()
