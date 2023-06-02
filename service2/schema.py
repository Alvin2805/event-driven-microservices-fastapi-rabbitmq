from pydantic import BaseModel

class UserDetailRequest(BaseModel):
    fullname:str
    company:str
    username:str
    address:str
    email:str

class UserSchema(UserDetailRequest):
    id:int

    class Config:
        orm_mode = True