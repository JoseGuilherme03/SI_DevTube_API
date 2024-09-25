from sqlalchemy.orm import Session
from app.models.entities import Video
from http import HTTPStatus

from app.schemas.request import VideoSchema


def create_video_controller(db: Session, video: VideoSchema):
    db_video = Video(
        title=video.title,
        url=video.url,
        description=video.description,
        category_id=video.category_id,
    )
    db.add(db_video)
    db.commit()

    return db_video


def list_videos_controller(db: Session):
    return db.query(Video).all()


def read_video_controller(db: Session, video_id: int):
    query = db.query(Video).filter(Video.id == video_id).first()

    if not query:
        return {"msg": "Video not found", "status_code": HTTPStatus.NOT_FOUND}

    return query
