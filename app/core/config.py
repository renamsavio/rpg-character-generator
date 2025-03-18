from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "RPG Character Generator API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "API para geração de personagens de RPG"

settings = Settings()