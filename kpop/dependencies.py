from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from starlette import status

from kpop.config import API_SECRET_KEY, API_SECRET_KEY_NAME

api_secret_key_header_auth = APIKeyHeader(name=API_SECRET_KEY_NAME, auto_error=True)

async def authenticated(api_secret_key_header: str = Security(api_secret_key_header_auth)):
    if api_secret_key_header != API_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
