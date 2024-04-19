from fastapi import FastAPI
from models import Flowers

from database import *

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def about():
    return {"Hello": "Flowers World!!!"}


@app.get("/flowers/", response_model=list[Flowers])
def get_all_flowers(item: Flowers):
    return {"item": "здесь будут все цветы!!",
            "item_name": item.name,
            "item_description": item.description
            }


@app.get("/flowers/{flower_id}", response_model=Flowers)
def get_flower(flower_id: int, item: Flowers):
    return {"item_id": flower_id,
            "item_name": item.name,
            "item_description": item.description
            }
