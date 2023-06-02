from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

connection_url = "postgresql://nomad2805:Zhiff%40hmi3310@host.docker.internal:5432/mytesting"

engine = create_engine(connection_url)

session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()

