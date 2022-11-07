from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "wowwhataname"

    user_id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, index=True)
    superpower = Column(String)
