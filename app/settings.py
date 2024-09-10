from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    SECRET_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8')


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
