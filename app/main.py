from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from app.controllers.video_controller import create_video_controller, list_videos_controller, read_video_controller, \
    list_categories_controller
from app.internal_modules.database import engine, Base, session, get_db
from app.models.entities import User
from app.schemas.request import VideoSchema

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/videos/", response_model=VideoSchema)
def create_video(video: VideoSchema, db: Session = Depends(get_db)):
    return create_video_controller(db, video)


@app.get("/videos/")
def read_videos(db: Session = Depends(get_db)):
    return list_videos_controller(db)


@app.get("/videos/{video_id}")
def read_video(video_id: int, db: Session = Depends(get_db)):
    return read_video_controller(db, video_id)


@app.get("/categories/")
def get_cateogories(db: Session = Depends(get_db)):
    return list_categories_controller(db)
