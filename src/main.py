from file import get_file, write_file
from classes.train_data import TrainData

def get(message: str):
    return 'test'

def post(newDataTraining: TrainData):
    current_objetives = get_file()
    current_objetives['objectives'].append(newDataTraining.dict())
    write_file(current_objetives)
    return "Novo treinamento incluido!"
