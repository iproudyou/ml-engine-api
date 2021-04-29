from fastapi import APIRouter, Security
import redis

from kpop.config import settings
from kpop.celery.tasks import move_to_next_stage
from kpop.deps import authenticated
from kpop.metadata import STAGING, STAGING_TIME

redis_store = redis.Redis.from_url(settings.REDIS_STORE_CONN_URI)

router = APIRouter(
    prefix="/singers",
    tags=["singers"],
    dependencies=[Security(authenticated, scopes=['openid'])],
    responses={404: {"description": "Not found"}},
)


@router.get("/buy/{name}")
async def buy(name: str):
    for i in range(0, 5):
        move_to_next_stage.apply_async((name, STAGING[i]), countdown=i*STAGING_TIME)
    return True


@router.get("/status/{name}")
async def status(name: str):
    return redis_store.get(name)