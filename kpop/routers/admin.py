from fastapi import APIRouter, Security

from kpop.deps import authenticated

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Security(authenticated, scopes=['openid'])],
    responses={418: {"description": "I'm a teapot"}},
)

@router.post("/")
async def update_admin():
    return {"message": "Admin getting schwifty"}