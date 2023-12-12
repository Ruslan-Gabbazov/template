import functools
import os
import platform

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Класс настроек проекта: импорт параметров из .env
    и установка значений по умолчанию.
    """

    root_dir: str = os.path.abspath(__file__ + 3 * "/..")
    src_dir: str = os.path.join(root_dir, "src")

    server_host: str = "0.0.0.0"
    server_port: int = 8000

    ENVIRONMENT: str = "local"

    CORS_ALLOW_ORIGIN_LIST: str = "http://127.0.0.1:8000"

    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "template-app"
    POSTGRES_PASSWORD: str = "template-app"
    POSTGRES_DB: str = "template-app"

    @functools.cached_property
    def cors_allow_origins(self) -> list[str]:
        return self.CORS_ALLOW_ORIGIN_LIST.split("&")

    @functools.cached_property
    def postgres_host(self) -> str:
        if platform.system() == "Linux":
            return "template-db"
        else:
            return self.POSTGRES_HOST

    @functools.cached_property
    def postgres_dsn(self) -> str:
        database = self.POSTGRES_DB if self.ENVIRONMENT != "test" else f"{self.POSTGRES_DB}_test"
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.postgres_host}:{self.POSTGRES_PORT}/{database}"
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@functools.lru_cache()
def settings():
    return Settings()
