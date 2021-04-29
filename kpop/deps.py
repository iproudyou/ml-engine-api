import boto3
import boto3.session
from botocore.client import BaseClient
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from starlette import status

from kpop.config import settings

api_secret_key_header_auth = APIKeyHeader(name=settings.API_SECRET_KEY_NAME, auto_error=True)

async def authenticated(api_secret_key_header: str = Security(api_secret_key_header_auth)):
    if api_secret_key_header != settings.API_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
        
async def aws_session() -> BaseClient:
    session = boto3.session.Session(
        region_name = settings.AWS_S3_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    return session
