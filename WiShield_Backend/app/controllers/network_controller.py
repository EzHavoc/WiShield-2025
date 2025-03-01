from fastapi import APIRouter, Depends
from app.utils.network_scanner import scan_network
from app.middleware.auth_middleware import auth_required

router = APIRouter()

@router.get("/scan", dependencies=[Depends(auth_required)])
def scan():
    return {"devices": scan_network()}
