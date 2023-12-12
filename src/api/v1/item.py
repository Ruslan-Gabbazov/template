from typing import Sequence

from fastapi import APIRouter, Depends, status

from schemas.item import ItemSchema
from services.item import ItemService

router = APIRouter(prefix="/items", tags=["items"])


@router.get("", status_code=status.HTTP_200_OK, response_model=ItemSchema)
async def get_items(item_service: ItemService = Depends()) -> Sequence[ItemSchema]:
    return await item_service.get_items()
