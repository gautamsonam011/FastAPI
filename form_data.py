from fastapi import FastAPI, Form
from pydantic import BaseModel


app = FastAPI()
# form data =============> pip install python-multipart

@app.post("/form/data")
async def form_fun(username:str = Form(), password:str = Form()):
    return ({"username":username,"password":password})