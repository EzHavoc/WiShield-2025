from fastapi import APIRouter, WebSocket
from app.utils.websocket_manager import ws_manager

router = APIRouter()

@router.websocket("/ws/security-alerts")
async def websocket_endpoint(websocket: WebSocket):
    """Handles WebSocket connections for real-time security alerts."""
    await ws_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep connection alive
    except Exception:
        ws_manager.disconnect(websocket)
