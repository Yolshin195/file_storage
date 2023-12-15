from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def now_utc():
    return datetime.now()


class BaseEntity(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, unique=True, nullable=False)
    created: Mapped[datetime] = mapped_column(default=now_utc)
    updated: Mapped[datetime] = mapped_column(default=now_utc, onupdate=now_utc)
