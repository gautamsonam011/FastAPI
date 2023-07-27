from fastapi import FastAPI,Depends
from typing import Optional
from pydantic import BaseModel
from models import Base,product
from db import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
class ModelSchema(BaseModel):
    Product_Name:str
    Product_Brand:str
    Product_Price:float
    Product_description:str
    class config:
        orm_mode = True
        
        
class Items(BaseModel):
    None
    

@app.get("/product/")
def all_show(db:Session = Depends(get_db)):
    data = db.query(product).all()
    return data
    
@app.post("/product/")
def add_data(request:ModelSchema, db:Session = Depends(get_db)):
    data1 = {
        "Product_Name":request.Product_Name,
        "Product_Brand":request.Product_Brand,
        "Product_Price":request.Product_Price,
        "Product_description":request.Product_description
    }
    p = product(**data1)
    db.add(p)
    db.commit()
    return ("Added Data Successfully",p)
    
@app.get("/product/{id:int}")
def get_data(id:int, db:Session = Depends(get_db)):
    g = db.query(product).filter(product.id == id).first()
    return ("Get Data Successfully",g)
    
@app.put("/product/{id}")
def update_data(id:int, request:ModelSchema, db:Session = Depends(get_db)):
    u = db.query(product).filter(product.id == id).update({
        product.Product_Name: request.Product_Name,
        product.Product_Brand:request.Product_Brand,
        product.Product_Price :request.Product_Price,
        product.Product_description:request.Product_description 
        
    })
    # u.id = product.id 
    # u.Product_Name = product.Product_Name
    # u.Product_Brand = product.Product_Brand
    # u.Product_Price = product.Product_Price
    # u.Product_description = product.Product_description
    db.commit()
    return ("Updated Data Successfully",u)
    
@app.delete("/items/{id:int}")
def delete_data(id:int, db:Session = Depends(get_db)):
    d = db.query(product).filter(product.id == id).delete()
    db.commit()
    return ("Deleted Data Successfully")
    
    