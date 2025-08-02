# app/core/middleware.py
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from app.core.config import settings
from fastapi import Request

# Register global middlewares
def register_middlewares(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    if settings.ENV == "production":
        app.add_middleware(HTTPSRedirectMiddleware)

# Security headers
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers.update({
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "Strict-Transport-Security": "max-age=63072000; includeSubDomains; preload",
        "Referrer-Policy": "no-referrer",
        "Permissions-Policy": "geolocation=(), microphone=()"
    })
    return response

# Request logging
import logging
async def log_requests(request: Request, call_next):
    try:
        response = await call_next(request)
        if response.status_code >= 400:
            logging.error(
                f"Error {response.status_code} | Request: {request.method} {request.url.path} | "
                f"Query: {request.query_params} | Headers: {dict(request.headers)}"
            )
        return response
    except Exception as exc:
        logging.error(
            f"Exception: {exc} | Request: {request.method} {request.url.path} | "
            f"Query: {request.query_params} | Headers: {dict(request.headers)}"
        )
        raise