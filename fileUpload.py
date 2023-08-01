from fastapi import FastAPI, File, UploadFile, Request,Form

app = FastAPI()

# How To Upload File!!?> ================>

@app.post("/file/len")      # We can find len of file
async def file_bytes_len(file:bytes = File()):  # import File
    return ({"file":len(file)}) 

@app.post("/file/upload")
async def file_upload(file:UploadFile):
    return ({"file":file})

@app.post("/file/upload")
async def file_upload(file:UploadFile):
    return ({"file_name":file.filename,"file_content_name":file.content_type})

@app.post("/form/data/filedata")
async def formdata_uploadfile(file1:UploadFile,file2:bytes = File(),name:str = Form()):  # We can find file name, len and post name
    return ({"file_name":file1.filename, "file2_bytes":len(file2),"name":name})