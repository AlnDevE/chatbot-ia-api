import mysql.connector


def get_db():
    if not db:
        get_db()
    else:
        return db


def get_config():
    global db
    
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    
    return db