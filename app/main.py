from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.controllers.video_controller import create_video_controller, list_videos_controller, read_video_controller
from app.internal_modules.database import engine, Base, session, get_db
from app.models.entities import User
from app.schemas.request import VideoSchema

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.post("/videos/", response_model=VideoSchema)
def create_video(video: VideoSchema, db: Session = Depends(get_db)):
    return create_video_controller(db, video)


@app.get("/videos/")
def read_videos(db: Session = Depends(get_db)):
    return list_videos_controller(db)


@app.get("/videos/{video_id}")
def read_video(video_id: int, db: Session = Depends(get_db)):
    return read_video_controller(db, video_id)