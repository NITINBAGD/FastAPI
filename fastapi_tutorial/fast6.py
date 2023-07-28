from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name :str
    Description:str |None = None
    price:float
    tax : float | None=None


@app.post('/items')

def create_item(item : Item):
    return item