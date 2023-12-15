from uuid import UUID

from pydantic import BaseModel


class FileModel(BaseModel):
    file_id: UUID
    filename: str
    size: int


class PathFileModel(BaseModel):
    path: str
    filename: str
