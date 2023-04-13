from peewee import Model
from database.db import get_db

class BaseModel(Model):
    class Meta:
        database = get_db()