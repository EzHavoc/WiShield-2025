from fastapi import APIRouter, Depends, HTTPException, Header
from app.middleware.auth_middleware import validate_token

router = APIRouter()

@router.get("/validate")
def validate_access(authorization: str = Header(None)):
    """Endpoint to validate the provided token."""
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization token required")
    
    token = authorization.replace("Bearer ", "")  # Extract token from "Bearer <token>"
    if not validate_token(token):
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    return {"message": "Token is valid"}
