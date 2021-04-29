from fastapi import FastAPI, Request, Response, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from kpop.routers import admin, singers, items, instagrams
from kpop.deps import authenticated
from kpop.metadata import TAGS_OPENAPI_DOCS
from kpop.config import settings

app= FastAPI(title="KPOP API", docs_url='/openapidocs', openapi_tags=TAGS_OPENAPI_DOCS, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# app.add_middleware(HTTPSRedirectMiddleware)
# app.add_middleware(TrustedHostMiddleware, allowed_hosts=[settings.API_SERVER_URI])

app.include_router(singers.router)
app.include_router(items.router)
app.include_router(instagrams.router)
app.include_router(admin.router)


