
from peewee import *

db = None

def get_db():
    if not db:
        get_config()
    return db


def get_config():
    global db
    
    db = MySQLDatabase(
        host="yourhost",
        port=3306, 
        user="youruser",
        password="yourpassword",
        database="yourschema"
    )
    
    return db