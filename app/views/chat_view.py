from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.controllers.chat_controller import chat_controller

router = APIRouter()

@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await chat_controller.handle_connection(websocket)