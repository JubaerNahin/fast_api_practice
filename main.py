from enum import Enum
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

# So basically what this enum does is it restrics to select only the fixed allowed value
# from the list given to it 
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def read_model_name(model_name : ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name , "message" : "This is alexnet"}
    if model_name.value == "resnet":
        return {"model_name" : model_name , "message": "This is Resnet "}
    return {"model_name" : model_name ,  "message" : "This is lenet"}


@app.put("/{id}")
def read_root(id : int ,hello : str):
    return { "hello" : hello , "id" : id }

@app.get("/getItem")
def getItem():
    return item1

@app.get("/items/{item_id}")
def read_item(item_id : int , q : str) :
    return {'item_id' : item_id , "q" : q}

@app.put("/items/{item_id]}")
def update_item(item_id : int , item : Item):
    return {"item_name": item.name, "item_id": item_id}