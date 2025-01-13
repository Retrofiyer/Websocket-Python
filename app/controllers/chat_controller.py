from fastapi.websockets import WebSocket

class ChatController:
    def __init__(self):
        self.connections = []

    async def handle_connection(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                for connection in self.connections:
                    await connection.send_text(data)
        except Exception:
            self.connections.remove(websocket)

chat_controller = ChatController()