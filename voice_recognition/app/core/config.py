import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    API_VERSION: str = "v1" 
    API_V1_STR: str = f"/api/{API_VERSION}"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 180
    API_WIT_AI_ENDPOINT: str
    BASE_TOKEN: str
    class Config:
            case_sensitive = True
            env_file = os.path.expanduser("~/.env")

settings = Settings()