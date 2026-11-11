from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    app_name: str = "Gestion Business API"
    app_version: str = "0.1.0"
    app_description: str = "API de gestion d'entreprise inspirée de Square."
    environment: str = "dev"

    database_url: str = "sqlite:///./dev.db"

@lru_cache
def get_settings()-> Settings:
    return Settings()