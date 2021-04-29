import os

# Database config
DATABASE_CONNECTION_URI = os.environ['DATABASE_CONNECTION_URI']

# App config
API_SERVER_URI = os.environ['API_SERVER_URI']
API_SECRET_KEY = os.environ['API_SECRET_KEY']
API_SECRET_KEY_NAME =  os.environ['API_SECRET_KEY_NAME']
stages = ["confirmed", "shipped", "in transit", "arrived", "delivered"]
STAGING_TIME = 15 # seconds

# Rabbitmq config
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_USERNAME = os.environ.get('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')

# Redis config
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_CELERY_DB_INDEX = os.environ.get('REDIS_CELERY_DB_INDEX')
REDIS_STORE_DB_INDEX = os.environ.get('REDIS_STORE_DB_INDEX')

# Celery config
BROKER_CONN_URI = f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}"
BACKEND_CONN_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB_INDEX}"
REDIS_STORE_CONN_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_STORE_DB_INDEX}"

    