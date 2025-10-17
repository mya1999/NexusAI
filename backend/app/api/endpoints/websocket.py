from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List
import json
import asyncio
from datetime import datetime

router = APIRouter(prefix="/ws", tags=["WebSocket"])


class ConnectionManager:
    """Manage WebSocket connections"""
    
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                pass


manager = ConnectionManager()


@router.websocket("/data")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time data updates"""
    await manager.connect(websocket)
    
    try:
        while True:
            # Simulate real-time data streaming
            data = {
                "timestamp": datetime.utcnow().isoformat(),
                "value": 100 + (hash(str(datetime.utcnow())) % 50),
                "category": "realtime"
            }
            
            await websocket.send_json(data)
            await asyncio.sleep(2)  # Send updates every 2 seconds
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
