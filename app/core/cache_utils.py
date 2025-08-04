from app.core.config import settings

def cache_dependency():
    if not FastAPICache.get_backend():
        if settings.ENV.lower() == "production":
            FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
        else:
            FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")