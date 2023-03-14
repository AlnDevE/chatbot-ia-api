from file import get_file, write_file
from classes.train_data import TrainData
from train import train_ia

def get(message: str):
    return 'test'

def post(newDataTraining: TrainData):
    current_objetives = get_file()
    if(current_objetives and 'objectives' in current_objetives):  
        current_objetives['objectives'].append(newDataTraining.dict())
    else:
        current_objetives = {
            "objectives": [newDataTraining.dict()]
        }
    write_file(current_objetives)
    train_ia()
    return "Novo treinamento incluido!"
