import redis

from kpop.celery.worker import celery
from kpop.config import settings

redis_store = redis.Redis.from_url(settings.REDIS_STORE_CONN_URI)


@celery.task
def move_to_next_stage(name, stage):
    redis_store.set(name, stage)
    return stage