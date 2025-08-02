from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, Depends, Request
from app.limiter import limiter

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Example: Verify JWT token (replace with your actual JWT verification logic)
def verify_token(token: str = Depends(oauth2_scheme)):
    # Replace this with your real JWT validation logic
    if not token or token != "your-secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Optionally, return user info from token here

# Apply rate limiting to all endpoints in this router
def rate_limit(request: Request):
    return limiter.limit("100/minute")(lambda req: None)(request)