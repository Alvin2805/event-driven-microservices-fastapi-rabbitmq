from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import get_db
from model import UserDetail
from schema import UserDetailRequest
import requests
import json
from producer import SendEventMsg

router = APIRouter()

@router.get("/user-detail")
async def get_users(db:Session=Depends(get_db)):
    user_details = select(UserDetail)
    return db.scalars(user_details).all()

@router.post("/user-detail")
async def post_user(req:UserDetailRequest,db:Session=Depends(get_db)):
    new_data = UserDetail()
    new_data.fullname = req.fullname
    new_data.company = req.company
    new_data.username = req.username
    new_data.address = req.address

    check_addr = SendEventMsg()
    the_addr = {
        "address" : new_data.address
    }

    add_response = check_addr.call(the_addr,"service2")
    print("Got the response : %r" %add_response)

    new_data.email = req.email

    check_msg = SendEventMsg()
    the_msg = {
        "username" : new_data.username,
        "email" : new_data.email
    }
    
    response = check_msg.call(the_msg,"service1")
    print("Got the response : %r" %response)

    check_msg.connection.close()

    '''
    inp_data = {
        "username": new_data.username,
        "password": "Img" + new_data.username,
        "email": new_data.email
    }

    enc_data = json.dumps(inp_data)

    post_user = requests.post("http://127.0.0.1:8050/user",data=enc_data)

    new_data.login_id = post_user.json()["id"]
    '''

    new_data.login_id = int(response)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data

@router.get("/test-rabbitmq")
async def test_events():
    check_msg = SendEventMsg()
    the_msg = {
        "username" : "50642",
        "email" : "nomad2805@gmail.com"
    }
    
    response = check_msg.call(the_msg)
    print("Got the response : %r" %response)

    check_msg.connection.close()

    return {
        "The data received" : response
    }