from pydantic import BaseSettings


class Settings(BaseSettings):
    # db config
    database_type: str
    database_username: str
    database_password: str
    database_host: str
    database_port: int
    database_name: str

    # jwt
    secret_key: str
    algorithm: str
    access_token_expire_minutes : int

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
