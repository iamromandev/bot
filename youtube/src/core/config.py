from enum import Enum

from functools import cached_property, lru_cache

from pydantic import BaseSettings


class Env(str, Enum):
    local = "local"
    dev = "dev"
    stage = "stage"
    prod = "prod"


class Config(BaseSettings):
    env: Env
    debug: bool

    db_name: str
    db_user: str
    db_password: str
    db_port: int
    db_host: str
    live_ids: list

    @cached_property
    def db_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        keep_untouched = (cached_property,)
        env_file = ".env"
        use_enum_values = True


@lru_cache
def get_config() -> Config:
    return Config()