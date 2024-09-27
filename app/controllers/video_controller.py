from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.entities import Video, Category
from http import HTTPStatus

from app.schemas.request import VideoSchema, CategorySchema


def create_video_controller(db: Session, video: VideoSchema):
    db_category = db.query(Category).filter(Category.id == video.category_id).first()

    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    db_video = Video(
        title=video.title,
        url=video.url,
        description=video.description,
        category_id=video.category_id,
    )

    db.add(db_video)
    db.commit()
    db.refresh(db_video)

    return db_video


def create_category_controller(db: Session, category: CategorySchema):
    db_category = db.query(Category).filter(Category.name == category.name).first()
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    new_category = Category(name=category.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


def list_videos_controller(db: Session):
    return db.query(Video).all()


def list_categories_controller(db: Session):
    return db.query(Category).all()
