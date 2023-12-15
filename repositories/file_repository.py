from .base_repository import BaseRepository
from entities.file_entity import FileEntity


class FileRepository(BaseRepository):
    model_type = FileEntity
