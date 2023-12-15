from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
import db


class BaseService:
    def __init__(self, session: AsyncSession = Depends(db.get_session)):
        self.session: AsyncSession = session

        self.__init__post__()

    def __init__post__(self):
        pass
