"""App instance configs"""
 
import os

class BaseConfig:
    # Database config
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    host = os.environ['POSTGRES_HOST']
    database = os.environ['POSTGRES_DB']
    port = os.environ['POSTGRES_PORT']
    DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

    # App config
    API_SECRET_KEY = os.environ['API_SECRET_KEY']
