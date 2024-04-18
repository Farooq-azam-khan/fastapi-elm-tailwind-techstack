import time

from fastapi import APIRouter

from lib.types import User

api_router = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "api route not found..."}},
)


@api_router.post("/user")
def get_user(user: User):
    time.sleep(1)
    return ["here is a user"]
