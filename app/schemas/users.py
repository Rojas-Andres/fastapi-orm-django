from datetime import datetime

from pydantic import BaseModel


class CreateUser(BaseModel):
    email: str
    cellphone: str
    name: str


class UsersResponse(BaseModel):
    name: str
    email: str
    cellphone: str
    created_at: datetime
    updated_at: datetime
