from typing import List

from fastapi import FastAPI

from api.schemas.users import CreateUser, UsersResponse
from db.models import Users

app = FastAPI(
    title="FastApi with ORM django",
    description="Integracion de fastapi con orm de django",
)


@app.get("/users")
def get_users() -> List[UsersResponse]:
    users = Users.objects.all()
    return [
        UsersResponse(
            name=user.name,
            email=user.email,
            cellphone=user.cellphone,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
        for user in users
    ]


@app.post("/users")
def post_users(user: CreateUser):
    user_db = Users.objects.create(
        name=user.name,
        email=user.email,
        cellphone=user.cellphone,
    )
    user_db.save()
    return {
        "message": "User created successfully",
    }
