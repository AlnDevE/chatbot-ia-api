from models.pattern import Pattern
from models.response import Response
from models.training import Training
from classes.train_data import CreateTraining
import logging


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
    query = (Training.select(
        Training.id,
        Training.tag,
        Response.descricao.alias("pattern"),
        Pattern.descricao.alias("response")
        ).join(
        Response, on=(Response.training_id == Training.id)
    ).join(
        Pattern, on=(Pattern.training_id == Training.id)
    ).group_by(Training.id))
    
    all_datas = list(query.dicts())
    logging.debug(query)
    return "get"