from fastapi import FastAPI
from model import User
from database import engine
from controller import router

User.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.include_router(router)