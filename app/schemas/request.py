from typing import Optional
from pydantic import BaseModel


class VideoSchema(BaseModel):
    title: str
    url: str
    description: Optional[str] = None
    category_id: int

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    username: str
    password: str


class CategorySchema(BaseModel):
    name: str

    class Config:
        orm_mode = True
