from functools import cached_property
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict
from system.constants import Environment


class Settings(BaseSettings):
    # Allow use cached_property
    model_config = SettingsConfigDict(ignored_types=(cached_property,))

    # Env
    ENVIRONMENT: Environment = Environment.development
    
    # HTTP
    BACKEND_PROTOCOL: Literal["http", "https"] = "http"
    BACKEND_HOST: str = "localhost"
    BACKEND_PORT: int = 8881
    BACKEND_API_PREFIX: str = "api/v1"
    FRONTEND_URL: str = "http://0.0.0.0:8880/"

    @cached_property
    def DEV_MODE(self) -> bool:  # noqa: N802
        return self.ENVIRONMENT == Environment.development