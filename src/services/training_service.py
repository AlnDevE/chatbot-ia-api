from models.pattern import Pattern
from models.response import Response
from models.training import Training
from classes.train_data import CreateTraining
import logging
from classes.train_data import TrainData


def post(data: CreateTraining):
    all_tags = [training["tag"] for training in list(Training.select(Training.tag).dicts())] 
    if data.tag in all_tags:
        raise Exception
    pk = Training.create(tag=data.tag)._pk
    [
        Pattern.create(
                descricao=pattern,
                training_id= pk
        )
        for pattern in data.patterns
    ]
    [
        Response.create(
            descricao=response,
            training_id= pk
        )
        for response in data.responses
    ]
    logging.info("Created")
    return "post OK"

def put():
    return "put"

def delete():
    return "delete"

def get():
    logging.debug("-> GETTING DATA")
    all_trainings = list(Training.select().dicts())
    all_patterns = list(Pattern.select().dicts())
    all_responses = list(Response.select().dicts())
    
    return group_data(all_trainings, all_patterns, all_responses)


def group_data(all_trainings, all_patterns, all_responses):
    logging.debug("-> GROUPING DATA")
    grouped: list[TrainData] = []
    for training in all_trainings:
        list_of_pattern_by_id = [
            data["descricao"] for data in 
            list(filter(lambda data: data["training_id"] == training["id"], all_patterns))
        ]
        list_of_response_by_id = [
            data["descricao"] for data in 
            list(filter(lambda data: data["training_id"] == training["id"], all_responses))
        ]
        grouped.append({
            "id": training["id"],
            "tag": training["tag"],
            "patterns": list_of_pattern_by_id,
            "responses": list_of_response_by_id
        })
    return grouped