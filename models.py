from pydantic import BaseModel


class Flowers(BaseModel):
    name: str
    description: str
    price: float
