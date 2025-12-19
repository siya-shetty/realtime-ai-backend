from fastapi import WebSocket
from app.db import create_session, log_event
import time

async def session_socket(websocket: WebSocket, session_id: str):
    await websocket.accept()

    start_time = time.time()
    await create_session(session_id)

    try:
        while True:
            message = await websocket.receive_text()
            await log_event(session_id, "user_message", message)
            await websocket.send_text(f"Echo: {message}")
            await log_event(session_id, "ai_response", f"Echo: {message}")

    except Exception:
        duration = int(time.time() - start_time)
        print(f"Session {session_id} ended. Duration: {duration}s")


