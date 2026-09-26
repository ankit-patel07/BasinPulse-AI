# backend/websocket/realtime.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        """Puri application ya simulator se data lekar saare connected clients ko realtime bhejna"""
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                # Agar koi client disconnect ho gaya ho toh safe clean up
                pass

manager = ConnectionManager()

@router.websocket("/ws/live-stream")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Client se incoming text messages (agar koi dashboard control click ho) read karna
            data = await websocket.receive_text()
            # Respond baseline acknowledging command received
            await websocket.send_json({"status": "alive", "echo": data})
    except WebSocketDisconnect:
        manager.disconnect(websocket)