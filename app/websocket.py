from fastapi import WebSocket

async def session_socket(websocket: WebSocket, session_id: str):
    await websocket.accept()
    
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(f"Echo: {message}")
    except Exception:
        print(f"Session {session_id} disconnected")
