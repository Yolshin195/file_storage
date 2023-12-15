from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base_entity import BaseEntity


class FileEntity(BaseEntity):
    __tablename__ = "file"

    name: Mapped[str] = mapped_column(String(512))
    tag: Mapped[str]
    size: Mapped[int]
    mimetypes: Mapped[str]
    path: Mapped[str]
