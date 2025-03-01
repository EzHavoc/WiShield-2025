import os
from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session
from app.utils.network_scanner import scan_network
from app.models.privacy_log import PrivacyLog
from app.config.database import get_db
from app.middleware.auth_middleware import authenticate_user
from app.websocket import send_alert

async def detect_threats(request: Request, db: Session = Depends(get_db), user: dict = Depends(authenticate_user)):
    try:
        network_data = scan_network()
        if "00:11:22:33:44:55" in network_data:  # Example rogue AP MAC
            log_entry = PrivacyLog(
                user_id=user["sub"],
                ip_address=request.client.host,
                violation_type="Rogue AP detected"
            )
            db.add(log_entry)
            db.commit()
            send_alert("privacy-alert", log_entry)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Network scanning failed")
