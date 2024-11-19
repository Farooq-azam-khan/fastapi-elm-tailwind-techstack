import time

from fastapi import APIRouter

from lib.types import User

user_router = APIRouter(
    prefix="/api",
    tags=["user_router"],
    responses={404: {"description": "api route not found..."}},
)


@user_router.get("/user")
def api_get_user():
    time.sleep(1)
    return ["here is a user"]


@user_router.post("/user")
def api_add_user(user: User):
    time.sleep(1)
    user.username += "[added]"
    return user
