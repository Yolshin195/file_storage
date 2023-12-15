import os
from uuid import UUID

from fastapi import APIRouter, UploadFile, Depends, HTTPException
from fastapi.responses import FileResponse

from models.file_model import FileModel
from services.file_service import FileService

file_router = APIRouter(prefix="/file", tags=["File"])


@file_router.post("/upload")
async def create_upload_file(file: UploadFile, file_service: FileService = Depends()) -> FileModel:
    return await file_service.save_file(file)


@file_router.get("/all")
async def get_all(skip: int = 0, limit: int = 100, file_service: FileService = Depends()) -> list[FileModel]:
    return await file_service.find_all(skip, limit)


@file_router.get("/find/by/id")
async def find_by_id(file_id: UUID, file_service: FileService = Depends()) -> FileModel:
    return await file_service.find_by_id(file_id)


@file_router.get("/download")
async def download(file_id: UUID, file_service: FileService = Depends()):
    file_entity = await file_service.read_file(file_id)
    if not os.path.exists(file_entity.path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_entity.path, filename=file_entity.filename)
