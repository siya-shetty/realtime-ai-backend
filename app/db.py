import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# ---- SESSION METADATA ----
async def create_session(session_id: str, user_id: str = "anonymous"):
    supabase.table("sessions").insert({
        "session_id": session_id,
        "user_id": user_id
    }).execute()

async def end_session(session_id: str, duration: int, summary: str):
    supabase.table("sessions").update({
        "end_time": "now()",
        "duration_seconds": duration,
        "summary": summary
    }).eq("session_id", session_id).execute()

# ---- EVENT LOGGING ----
async def log_event(session_id: str, event_type: str, content: str):
    supabase.table("session_events").insert({
        "session_id": session_id,
        "event_type": event_type,
        "content": content
    }).execute()
