from .base import BaseModel
from peewee import IntegerField, ForeignKeyField, TextField
from .training import Training


class Response(BaseModel):
    id = IntegerField(primary_key=True)
    training_id = ForeignKeyField(
        model=Training,
        field="id"
    )
    descricao = TextField(null=False)
    
    class Meta:
        db_table = 'response'