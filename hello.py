from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def hey():
    return {"Hello World":"Hey"}