import functools
import typing

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from core.config import settings


@functools.lru_cache
def get_engine(url: str | URL | None = None, **kwargs) -> AsyncEngine:
    return create_async_engine(url or settings().postgres_dsn, echo=False, future=True, **kwargs)


def get_async_session(
    url: str | URL | None = None,
) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(get_engine(url or settings().postgres_dsn), expire_on_commit=False)


async def get_session() -> typing.AsyncGenerator[AsyncSession, None]:
    async_session = get_async_session()
    async with async_session() as session:
        yield session
