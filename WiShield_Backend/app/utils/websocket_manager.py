from fastapi import WebSocket
from typing import List

class WebSocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """Accepts a new WebSocket connection."""
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """Removes a WebSocket connection when disconnected."""
        self.active_connections.remove(websocket)

    async def send_message(self, message: str):
        """Sends a message to all active WebSocket connections."""
        for connection in self.active_connections:
            await connection.send_text(message)

ws_manager = WebSocketManager()
