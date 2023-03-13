from fastapi import APIRouter, HTTPException
from src.main import get

router = APIRouter()

@router.get("/chat-fatec/response/")
def get_response(message): 
    if not message:
        raise HTTPException(404, "Has not message")
    try:
        return get(message)
    except Exception as exc:
        raise HTTPException(500, f"Internal server error")