from pydantic import BaseModel


class FileModel(BaseModel):
    filename: str
    size: int
