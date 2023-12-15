import os
from uuid import UUID

import aiofiles
from fastapi import UploadFile

from config import UPLOAD_DIR
from entities.file_entity import FileEntity
from models.file_model import FileModel, PathFileModel
from repositories.file_repository import FileRepository
from .base_service import BaseService


async def save_file(file: UploadFile) -> str:
    # TODO need include aiofiles.os
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    async with aiofiles.open(file_path, "wb") as f:
        while content := await file.read(1024):
            await f.write(content)
    return file_path


class FileService(BaseService):

    def __init__post__(self):
        self.repository = FileRepository(self.session)

    async def find_by_id(self, file_id: UUID) -> FileModel:
        return self.mapper(await self.repository.find_by_id(file_id))

    async def find_all(self, skip: int = 0, limit: int = 100) -> list[FileModel]:
        return [self.mapper(entity) for entity in await self.repository.find_all(skip, limit)]

    async def save_file(self, file: UploadFile) -> FileModel:
        file_path = await save_file(file)
        file_entity = FileEntity(
            name=file.filename,
            size=file.size,
            path=file_path,
            mimetypes=file.content_type,
            tag='test'
        )
        return self.mapper(await self.repository.add_one(file_entity))

    async def read_file(self, file_id: UUID) -> PathFileModel:
        file_entity = await self.repository.find_by_id(file_id)
        file_path = os.path.join(UPLOAD_DIR, file_entity.name)
        return PathFileModel(
            path=file_path,
            filename=file_entity.name
        )

    @staticmethod
    def mapper(entity: FileEntity) -> FileModel:
        return FileModel(
            file_id=entity.id,
            filename=entity.name,
            size=entity.size
        )
