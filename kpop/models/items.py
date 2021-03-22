from typing import TypedDict

from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date

from kpop.database import Base

class ItemDict(TypedDict):
    name: str
    price: int
    
class Item(Base):
    __tablename__ = "items"

    name = Column(String, primary_key=True)
    price = Column(Integer)

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"<Item {self.name}>"

    @property
    def serialize(self) -> ItemDict:
        return {"name": self.name, "price": self.price}
