import os
from pydantic import BaseSettings
from typing import Optional, Dict, Any, List

class Settings(BaseSettings):
    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "CodeCatalystAI"
    
    # Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "development_secret_key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Server settings
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./codecatalyst.db")
    
    # CORS settings
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    # File upload settings
    UPLOAD_DIRECTORY: str = os.getenv("UPLOAD_DIRECTORY", "uploads")
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10 MB
    
    # Repository integration settings
    GITHUB_API_URL: str = "https://api.github.com"
    GITLAB_API_URL: str = "https://gitlab.com/api/v4"
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
