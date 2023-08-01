from fastapi import FastAPI , UploadFile, File,Form,HTTPException

app = FastAPI()

# error handling------------>>

@app.get("/error/exception")
async def handlle_error(item:int):
    if item ==2:
        return HTTPException(status_code = 400,detail = "Item is not equal to 2 try another value!!")
    return ({"value":item})

items = [1,2,3,4,5,6]
@app.get("/error/exception1")
async def handlle_error1(item:int):
    if item not in items:
        return HTTPException(status_code = 400,detail = "Item is not equal to items try another value!!")
    return ({"value":item})