from typing import Sequence

from fastapi import Depends

from core.exceptions import item_not_found_exception
from db.repository.item import ItemRepository
from schemas.item import ItemSchema


class ItemService:
    def __init__(self, item_repository: ItemRepository = Depends()):
        self._item_repository = item_repository

    async def get_items(self) -> Sequence[ItemSchema]:
        items = await self._item_repository.get_items()

        if not items:
            raise item_not_found_exception

        return [
            ItemSchema(id=item.id, item_num=item.item_num, description=item.description, is_active=item.is_active)
            for item in items
        ]
