from models.pattern import Pattern
from models.response import Response
from models.training import Training
from classes.train_data import CreateTraining


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
    return "post OK"

def put():
    return "put"

def delete():
    return "delete"

def get():
    return "get"