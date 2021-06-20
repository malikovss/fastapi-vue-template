from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
async def hello():
    return {"message": "Hello World"}
