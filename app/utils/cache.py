from fastapi import Request

def user_token_cache_key(func, *args, **kwargs):
    request: Request = kwargs.get("request")
    token = request.headers.get("authorization", "")
    return f"{func.__module__}:{func.__name__}:{token}:{request.url.path}:{request.url.query}"