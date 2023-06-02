from pydantic import BaseModel

class AddressRequest(BaseModel):
    address:str

class AddressSchema(AddressRequest):
    id:int

    class Config:
        orm_mode = True