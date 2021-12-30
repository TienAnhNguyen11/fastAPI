from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Tien Anh, day la root"}


@app.get("/home")
async def home():
    return {"message": "Hello Tien Anh, day la home"}