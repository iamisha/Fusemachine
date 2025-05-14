from pydantic_settings import BaseSettings  # Changed import

class Settings(BaseSettings):
    app_name: str = "Calculator API"
    redis_url: str = "redis://localhost:6379"  # Local dev setting
    debug: bool = False

    class Config:
        env_file = ".env"
