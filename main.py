from fastapi import Body
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    price : float
    is_offer : bool | None = None

item1 = Item(
    name = "Item 1",
    price = 20.30,
    is_offer = True
)

# hello : int

@app.put("/")
def read_root(hello : int):
    return hello

@app.get("/getItem")
def getItem():
    return item1

@app.get("/items/{item_id}")
def read_item(item_id : int , q : str) :
    return {'item_id' : item_id , "q" : q}

@app.put("/items/{item_id]}")
def update_item(item_id : int , item : Item):
    return {"item_name": item.name, "item_id": item_id}