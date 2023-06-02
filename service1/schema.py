from pydantic import BaseModel

class UserRequest(BaseModel):
    username:str
    password:str
    email:str

class UserSchema(UserRequest):
    id:int

    class Config:
        orm_mode = True