```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/users/me")
def read_users_me():
    return {"username": "fastapi"}

@app.get("/users/{user_id}")
def read_users(user_id: str):
    return {"username": user_id}

@app.get("/items/")
def read_items(q: str = None, skip: int = 0, limit: int = 10):
    items = [{"item_id": i} for i in range(10)]
    if q:
        items = [item for item in items if q in str(item)]
    return items[skip : skip + limit]

@app.get("/items/{item_id}/description")
def read_description(item_id: int):
    return {"description": "This is a description"}

@app.post("/items/")
def create_item(item: Item):
    return item

@app.get("/items/{item_id}/price")
def read_price(item_id: int):
    return {"price": 10.99}

@app.get("/items/{item_id}/tax")
def read_tax(item_id: int):
    return {"tax": 0.99}

@app.put("/items/{item_id}/price")
def update_price(item_id: int, price: float):
    return {"price": price}

@app.put("/items/{item_id}/tax")
def update_tax(item_id: int, tax: float):
    return {"tax": tax}

@app.get("/items/{item_id}/name")
def read_name(item_id: int):
    return {"name": "Item Name"}

@app.put("/items/{item_id}/name")
def update_name(item_id: int, name: str):
    return {"name": name}

@app.get("/healthcheck")
def healthcheck():
    return JSONResponse(content={"status": "ok"}, media_type="application/json")

@app.get("/ready")
def ready():
    return JSONResponse(content={"status": "ready"}, media_type="application/json")
```