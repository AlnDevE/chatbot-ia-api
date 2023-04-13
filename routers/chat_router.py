from fastapi import APIRouter, HTTPException
from src.main import get, post
from classes.train_data import TrainData
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

@router.post("/chat-fatec/train/")
def get_response(newDataTraining: TrainData):
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