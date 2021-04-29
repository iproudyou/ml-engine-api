from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database config
    DATABASE_CONNECTION_URI: str

    # App config
    API_SERVER_URI: str
    API_SECRET_KEY: str
    API_SECRET_KEY_NAME: str

    # Scraper config
    INSTA_USER_NAME: str
    INSTA_SESSION_ID: str

    # AWS config
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_S3_REGION_NAME: str

    # Rabbitmq config
    RABBITMQ_HOST: str
    RABBITMQ_USERNAME: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_PORT: int

    # Redis config
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_CELERY_DB_INDEX: int
    REDIS_STORE_DB_INDEX: int

    # Celery config
    BROKER_CONN_URI: str
    BACKEND_CONN_URI: str
    REDIS_STORE_CONN_URI: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings(_env_file='.env', _env_file_encoding='utf-8')

    