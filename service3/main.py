from fastapi import FastAPI
from model import Address
from database import engine
from controller import router

Address.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/")

app.include_router(router)