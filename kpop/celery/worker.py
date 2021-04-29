from celery import Celery

from kpop.config import settings

celery = Celery(
        "worker",
        broker=settings.BROKER_CONN_URI,
        backend=settings.BACKEND_CONN_URI,
        include=["kpop.celery.tasks"]
)