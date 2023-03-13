import json
from classes.train_data import TrainData

def get(message: str):
    return 'test'

def post(newDataTraining: TrainData):
    current_objetives_file = open('../objectives.json').read()
    current_objetives = json.loads(current_objetives_file)
    return current_objetives
    