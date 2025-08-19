from fastapi import APIRouter, Depends

from cryptway.auth.service import auth_by_api_key


router = APIRouter(
    dependencies=[Depends(auth_by_api_key)]
)


@router.get("/users/{user_id}")
async def get_user(user_id: int):
    pass


@router.post("/users")
async def add_user(user_id: int, username: str):
    pass


@router.patch("/users/{user_id}")
async def update_user(api_token: str, user_id: int):
    pass