from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Flower(BaseModel):
    name: str
    description: str
    price: float


@app.get("/")
def about():
    return {"Hello": "Flowers World!!!"}


@app.get("/flowers/")
def get_all_flowers(item: Flower):
    return {"item": "здесь будут все цветы!!",
            "item_name": item.name,
            "item_description": item.description
            }


@app.get("/flowers/{flower_id}")
def get_flower(flower_id: int, item: Flower):
    return {"item_id": flower_id,
            "item_name": item.name,
            "item_description": item.description
            }
