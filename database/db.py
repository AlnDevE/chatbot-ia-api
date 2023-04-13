
from peewee import *

db = None

def get_db():
    if not db:
        get_config()
    return db


def get_config():
    global db
    
    db = MySQLDatabase(
        host="localhost",
        port=3306,
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    
    return db