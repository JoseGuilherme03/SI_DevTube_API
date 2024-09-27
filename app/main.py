from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from app.controllers.video_controller import create_video_controller, list_videos_controller, list_categories_controller
from app.internal_modules.database import engine, Base, get_db
from app.models.entities import User
from app.schemas.request import VideoSchema, UserCreateSchema

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBasic()


def authenticate(credentials: HTTPBasicCredentials, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == credentials.username).first()
    if user is None or user.password != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user


@app.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = authenticate(credentials, db)
    return {"message": "Login successful"}


@app.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/videos/", response_model=VideoSchema)
def create_video(video: VideoSchema, db: Session = Depends(get_db),
                 credentials: HTTPBasicCredentials = Depends(security)):
    authenticate(credentials, db)
    return create_video_controller(db, video)


@app.get("/videos/")
def read_videos(db: Session = Depends(get_db)):
    return list_videos_controller(db)


@app.get("/categories/")
def get_categories(db: Session = Depends(get_db)):
    return list_categories_controller(db)
