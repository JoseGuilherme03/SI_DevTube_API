from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.internal_modules.database import Base


class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String, index=True)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="videos")


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)

    videos = relationship("Video", back_populates="category")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True)
    password = Column(String)
    role = Column(String, index=True)
