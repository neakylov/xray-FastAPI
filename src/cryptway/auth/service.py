from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

from passlib.context import CryptContext

from cryptway.config import API_KEY_HASH

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

api_key_header = APIKeyHeader(name="X-API-Key")


def verify_api_key(api_key):
    return pwd_context.verify(api_key, API_KEY_HASH)


def auth_by_api_key(api_key: str = Depends(api_key_header)):
    if not verify_api_key(api_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid X-API-Key"
        )
    return api_key