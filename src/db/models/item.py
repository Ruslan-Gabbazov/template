from sqlalchemy import Boolean, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import BaseModel
from db.models.mixins import CreatedAtMixin, IDMixin, UpdatedAtMixin


class Item(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin):
    item_num: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def __str__(self):
        return f"Item #{self.item_num} with id={self.id})"
