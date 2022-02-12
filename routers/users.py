from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Sanal"}, {"username": "Morty"}]


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "current user"}


@router.get("/users/{username}", tags=["users"])
async def read_users(username: str):
    return {"username": username}
