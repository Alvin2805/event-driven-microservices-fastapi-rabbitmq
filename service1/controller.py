from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import get_db
from model import User
from schema import UserRequest

router = APIRouter()

@router.get("/user")
async def get_users(db:Session=Depends(get_db)):
    users = select(User)
    return db.scalars(users).all()

@router.post("/user")
async def post_user(req:UserRequest,db:Session=Depends(get_db)):
    new_data = User()
    new_data.username = req.username
    new_data.password = req.password
    new_data.email = req.email
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data