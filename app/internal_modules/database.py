from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

usuario = 'postgres'
senha = '159263'
host = 'localhost'
porta = 5432
nome_bd = 'devtube_database'

DATABASE_URL = f"postgresql://{usuario}:{senha}@{host}:{porta}/{nome_bd}"

engine = create_engine(DATABASE_URL, echo=True)
session = sessionmaker(bind=engine, class_=Session, expire_on_commit=False)
Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
