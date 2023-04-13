
from peewee import *

db = None

def get_db():
    if not db:
        get_config()
    return db


def get_config():
    global db
    
    db = MySQLDatabase(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="sql.aln135",
        database="chatbot"
    )
    
    return db