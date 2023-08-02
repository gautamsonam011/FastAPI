from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import SessionLocal,engine
from model import Base


Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
class userSchema(BaseModel):
    pass

app = FastAPI()


@app.post("/")
def add_data():
    pass

@app.get("/")
def get_data():
    pass