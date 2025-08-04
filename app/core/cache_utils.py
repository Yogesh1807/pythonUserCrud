from app.core.config import settings
from fastapi_cache import FastAPICache

def cache_dependency():
    if not FastAPICache.get_backend():
        FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
      