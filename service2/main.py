from fastapi import FastAPI
from model import UserDetail
from database import engine
from controller import router

UserDetail.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.include_router(router)