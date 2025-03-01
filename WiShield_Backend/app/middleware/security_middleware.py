import os
from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session
from app.utils.network_scanner import scan_network
from app.models.network_log import NetworkLog
from app.config.database import get_db
from app.middleware.auth_middleware import authenticate_user
from app.utils.websocket_manager import ws_manager  # Import WebSocket manager

async def detect_threats(request: Request, db: Session = Depends(get_db), user: dict = Depends(authenticate_user)):
    """
    Detects network security threats, logs them in the database, and sends real-time alerts via WebSockets.
    """
    try:
        network_data = scan_network()

        # Example: Check for a Rogue AP using its MAC address
        if "00:11:22:33:44:55" in network_data:  
            log_entry = NetworkLog(
                user_id=user["sub"],
                ip_address=request.client.host,
                violation_type="Rogue AP detected"
            )
            db.add(log_entry)
            db.commit()

            # Send real-time alert via WebSockets
            alert_message = f"⚠️ Security Alert: Rogue AP detected from {request.client.host}"
            await ws_manager.send_message(alert_message)  

    except Exception as e:
        print(f"Error detecting threats: {e}")  # Helps debug issues
        raise HTTPException(status_code=500, detail="Network scanning failed")
