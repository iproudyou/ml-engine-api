from fastapi import APIRouter, Security
import redis

from kpop.config import stages, REDIS_STORE_CONN_URI, STAGING_TIME
from kpop.celery.tasks import move_to_next_stage
from kpop.dependencies import authenticated

redis_store = redis.Redis.from_url(REDIS_STORE_CONN_URI)

router = APIRouter(
    prefix="/singers",
    tags=["singers"],
    dependencies=[Security(authenticated, scopes=['openid'])],
    responses={404: {"description": "Not found"}},
)


@router.get("/buy/{name}")
async def buy(name: str):
    for i in range(0, 5):
        move_to_next_stage.apply_async((name, stages[i]), countdown=i*STAGING_TIME)
    return True


@router.get("/status/{name}")
async def status(name: str):
    return redis_store.get(name)