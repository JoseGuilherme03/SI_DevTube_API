from typing import Optional
from pydantic import BaseModel


class VideoSchema(BaseModel):
    title: str
    url: str
    description: Optional[str] = None
    category_id: int

    class Config:
        orm_mode = True
