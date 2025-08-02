# main.py
from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
from app.core.config import settings
from app.core.middleware import register_middlewares, add_security_headers, log_requests
from app.core.logging_config import configure_logging
from app.core.exceptions import sqlalchemy_exception_handler
from app.routes.user_route import router as user_router
from app.routes.log_route import router as log_router
from app.limiter import limiter
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.backends.inmemory import InMemoryBackend
from redis.asyncio import Redis
import time
# import logging

load_dotenv()

app = FastAPI()

# Middleware & Exception handlers
register_middlewares(app)
app.middleware("http")(add_security_headers)
app.middleware("http")(log_requests)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_exception_handler(Exception, sqlalchemy_exception_handler)

# Logging
configure_logging()

# Startup cache
@app.on_event("startup")
async def on_startup():
    if settings.ENV.lower() == "production":
        redis_instance = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
        FastAPICache.init(RedisBackend(redis_instance), prefix="fastapi-cache")
        # logging.info("Using Redis cache backend for production.")
    else:
        FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
        # logging.info("Using in-memory cache backend for development.")

# Routes
@app.get("/ping")
@limiter.limit("5/minute")
async def ping(request: Request):
    start = time.perf_counter()
    response = {"message": "pong"}
    duration = time.perf_counter() - start
    response["duration_ms"] = round(duration * 1000, 2)
    return response

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(log_router, prefix="/log", tags=["Log"])