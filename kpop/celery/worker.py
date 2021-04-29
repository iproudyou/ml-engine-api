from celery import Celery

from kpop.config import BACKEND_CONN_URI, BROKER_CONN_URI

celery = Celery(
        "worker",
        broker=BROKER_CONN_URI,
        backend=BACKEND_CONN_URI,
        include=["kpop.celery.tasks"]
)