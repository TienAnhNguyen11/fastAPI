from fastapi import FastAPI

car = FastAPI()


@car.get("/items/{item_id}")
async def read_item(item_id):
    return {"car type": item_id}