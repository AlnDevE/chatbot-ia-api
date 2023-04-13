from fastapi import APIRouter, HTTPException
from src.main import get
from src.services.training_service import post
from classes.train_data import CreateTraining
from train import get_trainings

router = APIRouter()

@router.get("/chat-fatec/response/")
def get_response(message): 
    if not message:
        raise HTTPException(404, "Has not message")
    try:
        return get(message)
    except Exception as exc:
        raise HTTPException(500, f"Internal server error")

@router.post("/chat-fatec/trainings/")
def get_response(newDataTraining: CreateTraining):
    if not newDataTraining:
        raise HTTPException(404, "Has not data training")
    try:
        return post(newDataTraining)
    except Exception as exc:
        raise HTTPException(500, f"Internal server error")

@router.get("/chat-fatec/trainings/")
def get_response(): 
    try:
        return get_trainings()
    except Exception as exc:
        raise HTTPException(500, f"Internal server error")