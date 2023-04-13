from .base import BaseModel
from peewee import IntegerField, TextField

class Training(BaseModel):
    id = IntegerField(primary_key=True)
    tag = TextField(unique=True)
    
    class Meta:
        db_table = 'training'