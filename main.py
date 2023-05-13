from typing import Union
from pydantic import BaseModel # to instruct the api to build a schema
from typing import Optional  # to handle any data type into our desired type
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class Customer(BaseModel):
    id: str
    name: Optional[str] = None
    email: Optional[str] = None
    phone: int


# endpoint in postman: http://localhost:5000/item
@app.get("/")
async def read_item():
    return {"message": "hello world"}

# endpoint in postman: http://localhost:5000/post 
@app.post("/post")
async def create_post(items: Item):
    received = items
    return {
        "status": "success",
        "data": received
    }
@app.post("/customer")
async def create_customer(items: Customer):
    received = items
    return {
        "status": "success",
        "data": received
    }



# start the app → uvicorn index:app --port 5000 --reload --log-level debug    

# cd to the code file then use python -m uvicorn filename:app(variable used to call FastApi) --reload
# example: PS D:\python_stuff> python -m uvicorn main:app --reload     