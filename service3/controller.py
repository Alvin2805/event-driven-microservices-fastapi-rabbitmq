from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import get_db
from model import Address
from schema import AddressRequest

router = APIRouter()

@router.get("/address")
async def get_addresses(db:Session=Depends(get_db)):
    addresses = select(Address)
    return db.scalars(addresses).all()

@router.post("/address")
async def post_address(req:AddressRequest,db:Session=Depends(get_db)):
    new_data = Address()
    new_data.address = req.address
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data