from typing import List

from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session

from kpop.database import engine, SessionLocal
from kpop.dependencies import authenticated
from kpop.models import items as model
from kpop.schemas import items as schema
from kpop.cruds import items as crud

model.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Security(authenticated)],
    responses={404: {"description": "Not found"}},
)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@router.get("/", response_model=List[schema.ItemBase])
def read_items(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    items = crud.get_items(session=session, skip=skip, limit=limit)
    return [i.serialize for i in items]


@router.get("/{name}", response_model=schema.ItemBase)
def read_item(name: str, session: Session = Depends(get_session)):
    item = crud.get_item_by_name(session=session, name=name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item.serialize