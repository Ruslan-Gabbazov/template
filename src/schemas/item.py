from pydantic import BaseModel


class ItemSchema(BaseModel):
    id: int
    item_num: int
    description: str
    is_active: bool
