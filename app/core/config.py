from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    PROJECT_NAME: str = "app"
    API_V1_PREFIX: str = "/api/v1"

    # Must use an async driver, e.g. postgresql+asyncpg://user:pass@host:5432/dbname
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/app"

    # Comma-separated list of allowed origins, e.g. "http://localhost:3000,https://example.com"
    BACKEND_CORS_ORIGINS: str = "*"

    @property
    def cors_origins(self) -> list[str]:
        if self.BACKEND_CORS_ORIGINS == "*":
            return ["*"]
        return [origin.strip() for origin in self.BACKEND_CORS_ORIGINS.split(",") if origin.strip()]


settings = Settings()