# app/core/exceptions.py
from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
import logging

async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    logging.error(f"SQLAlchemy error: {exc} | Request: {request.method} {request.url.path}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Database error occurred."}
    )