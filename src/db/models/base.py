import inflection
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, declarative_mixin


@declarative_mixin
class BaseModel(DeclarativeBase):
    """Base db model class."""

    @declared_attr
    def __tablename__(cls) -> str:
        """Generate __tablename__ automatically."""

        if cls.__name__[-1] == "y":
            name = cls.__name__[:-1] + "ies"
            return inflection.underscore(name)

        return inflection.underscore(cls.__name__) + "s"


POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}

BaseModel.metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)
