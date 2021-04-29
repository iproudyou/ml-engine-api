from fastapi import FastAPI, Request, Response, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from kpop.internal import admin
from kpop.routers import singers, items
from kpop.dependencies import authenticated
from kpop.metadata import tags_openapi_docs
from kpop.config import API_SERVER_URI

app= FastAPI(title="KPOP API", docs_url='/openapidocs', openapi_tags=tags_openapi_docs, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# app.add_middleware(HTTPSRedirectMiddleware)
# app.add_middleware(TrustedHostMiddleware, allowed_hosts=[API_SERVER_URI])

app.include_router(singers.router)
app.include_router(items.router)
app.include_router(admin.router)
