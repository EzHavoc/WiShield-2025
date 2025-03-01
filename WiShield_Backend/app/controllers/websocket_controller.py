from fastapi import WebSocket, WebSocketDisconnect
from typing import List

class WebSocketManager:
    """ Manages WebSocket connections for real-time security alerts. """
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """ Accepts new WebSocket connection. """
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """ Removes disconnected WebSocket. """
        self.active_connections.remove(websocket)

    async def send_message(self, message: str):
        """ Sends real-time security alert to all connected clients. """
        for connection in self.active_connections:
            await connection.send_text(message)

# Instantiate WebSocket Manager
ws_manager = WebSocketManager()
