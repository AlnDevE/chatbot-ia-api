from fastapi import APIRouter, HTTPException
from src.main import get_main
from src.services.training_service import post, get, delete
from classes.train_data import CreateTraining
import logging
from training_ia import tra_ia

router = APIRouter()

@router.get("/chat-fatec/response/")
def get_response(message): 
    if not message:
        raise HTTPException(404, "Has not message")
    try:
        return get_main(message)
    except Exception as exc:
        raise HTTPException(500, f"Internal server error")

@router.post("/chat-fatec/trainings/")
def post_training(newDataTraining: list[CreateTraining]):
    if not newDataTraining:
        raise HTTPException(404, "Has not data training")
    try:
        post(newDataTraining)
        logging.info("-> TRAINING STARTED")
        tra_ia()
        logging.info("-> TRAINING OK")
    except Exception as exc:
        raise HTTPException(500, f"Internal server error")

@router.get("/chat-fatec/trainings/")
def get_response(): 
    try:
        return get()
    except Exception as exc:
        raise HTTPException(500, f"Internal server error")

@router.delete("/chat-fatec/trainings/{training_id}")
def delete_training(training_id: int): 
    try:
        return delete(training_id)
    except Exception as exc:
        raise HTTPException(500, f"Internal server error")