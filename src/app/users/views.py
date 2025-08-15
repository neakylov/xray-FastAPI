from fastapi import APIRouter

router = APIRouter()


@router.get("/{api_token}/users/{user_id}")
async def get_user(api_token: str, user_id: int):
    if api_token:
        pass

@router.post("/{api_token}/users")
async def add_user(api_token: str, user_id: int, username: str):
    pass

@router.patch("/{api_token}/users/{user_id}")
async def update_user(api_token: str, user_id: int):
    pass