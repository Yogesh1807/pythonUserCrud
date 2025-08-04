from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

def ensure_cache():
    if not FastAPICache.get_backend():
        FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")