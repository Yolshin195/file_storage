import os

import aiofiles
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")


async def save_file(file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    async with aiofiles.open(file_path, "wb") as f:
        content = await file.read()
        await f.write(content)
    return file_path


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_path = await save_file(file)
    return {"filename": file.filename, "file_path": file_path}


@app.get("/files/")
async def read_files():
    files = os.listdir(UPLOAD_DIR)
    return {"files": files}


@app.get("/files/{file_name}")
async def read_file(file_name: str):
    file_path = os.path.join(UPLOAD_DIR, file_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, filename=file_name)