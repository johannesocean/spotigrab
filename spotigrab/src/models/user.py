from pydantic import BaseModel


class UserCreate(BaseModel):
    user_id: int
    name: str
    superpower: str


class User(BaseModel):
    user_id: int
    name: str
    superpower: str

    class Config:
        orm_mode = True
