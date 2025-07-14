from enum import Enum

from pydantic_settings import BaseSettings


class AppEnv(str, Enum):
    LOCAL = "LOCAL"
    PRODUCTION = "PRODUCTION"


class Settings(BaseSettings):
    APP_ENV: AppEnv = "LOCAL"
    # For consumption of Meteo France public APIs
    METEOFR_GEN_OAUTH_TOKEN_URL: str = "https://portail-api.meteofrance.fr/token"
    METEOFR_DPVIG_API_BASE_URL: str = (
        "https://public-api.meteofrance.fr/public/DPVigilance/v1"
    )
    METEOFR_DPVIG_APP_ID: str = "YOUR_APP_ID"


settings = Settings()
