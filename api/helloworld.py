from fastapi import FastAPI

app = FastAPI()

@app.get("/firstrouter")
async def hello():
    return "Hello World"