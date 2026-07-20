"""
Centralized, typed application settings.

Why pydantic-settings instead of os.getenv() scattered everywhere:
- Every setting is validated and typed at startup — a missing DATABASE_URL
  fails immediately with a clear error, not three files deep at runtime.
- Autocomplete + type checking everywhere Settings is used.
- One place to see everything the app depends on from the environment.
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # --- App ---
    app_env: str = Field(default="development")
    log_level: str = Field(default="INFO")

    # --- Database ---
    database_url: str

    # --- LLM ---
    anthropic_api_key: str = Field(default="")

    # --- Email ---
    smtp_host: str = Field(default="")
    smtp_port: int = Field(default=587)
    smtp_user: str = Field(default="")
    smtp_password: str = Field(default="")
    digest_recipient: str = Field(default="")

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"


@lru_cache
def get_settings() -> Settings:
    """
    Cached settings accessor.

    lru_cache means Settings() is only constructed once per process —
    every subsequent call to get_settings() returns the same instance
    instead of re-parsing the environment. Use this function everywhere
    you need config; don't import Settings() directly.
    """
    return Settings()