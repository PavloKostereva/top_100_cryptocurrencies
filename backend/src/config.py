from pydantic import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    CMS_API_KEY: str

    model_config= SettingsConfigDict(env_file=".env")

settings=Settings()    