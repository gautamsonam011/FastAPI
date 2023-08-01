from fastapi import FastAPI,Query,Path
from typing import Union
from enum import Enum
from pydantic import BaseModel
app_name = FastAPI()

# path-parameters-------------------->>>

@app_name.get("/item/{Item}")
def path_parameters(Item):
    var_name = {"path variable":Item}
    return (var_name)

# Query-parameters ------------------->>

@app_name.get("/query/")
def query_func(roll_no:int,name:str):
    var_std = {"roll_no":roll_no,"name":name}
    return (var_std)

@app_name.get("/query1/")
def query_func1(roll_no:int,name:str,age:Union[int,None]=None): # import Union
    var_std = {"roll_no":roll_no,"name":name, "age":age}
    return (var_std)

@app_name.get("/validation/")
def validation_func2(name:str,age:Union[str,None]= Query(min_length = 2,max_legth = 3)): # import Union and check validation
    var_std = {"name":name, "age":age}
    return (var_std)

# >>>>>>>>>>>>>>>>Enum>>>>>>>>>>>>

class Choice_Name(str, Enum):
    one = "Sonam"
    two = "Anjali"
    three = "Usha"
    
# @app_name.get("/choiceModel")
# def choice_model(model_name:Choice_Name):
#     return (model_name)
    
# @app_name.get("/choiceModel/{model_name}")
# def choice_model(model_name:Choice_Name):
#     if model_name.value =="one":
#         return {"model_name":model_name, "message":"Calling Sonam"}
#     elif model_name.value =="two":
#         return  {"model_name":model_name, "message":"Calling Anjali"}
#     else:
#          {"model_name":model_name, "message":"Calling Usha"}

@app_name.get("/models/{model_name}")
async def get_model(model_name:Choice_Name):
    if model_name.value == "one":
        return {"model_name":model_name, "message":"Calling Sonam"}
    elif model_name.value == "two":
        return {"model_name":model_name, "message":"Calling Anjali"}
    else:
        return {"model_name":model_name,"message":"Calling Usha"}
    
# ------------------------>>>>>>>>>>>>>>-------------- Pydantic import BaseModel

class Schema(BaseModel):
    roll_no:int
    name:str
    class_room:str
    
    
@app_name.post("/std/")
def post_data(item:Schema):
    return item
    

