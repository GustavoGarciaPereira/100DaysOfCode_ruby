from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from typing import List
from typing import Set, Tuple
from typing import Dict


app = FastAPI()


def main(user_id: str):
    return user_id


class User(BaseModel):
    id: int
    name: str
    joined: date


my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2018-11-30",
}

my_second_user: User = User(**second_user_data)


def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return {'items_t': items_t, 'items_s': items_s}


@app.get("/process/")
async def process_get():
    return process_items(items_t=(1, 2, 3), items_s='wer')


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
