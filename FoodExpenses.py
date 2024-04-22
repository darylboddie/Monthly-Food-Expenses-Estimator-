import sqlite3 as db

# Function to create a database 
def init():
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    create table if not exists expenses (
        amount number,
        category string,
        message string,
        date string
        )
    '''
    cur.execute(sql)
    conn.commit()
init()

def log(amount, category, message=""):
    from datetime import datetime
    date = str(datetime.now())
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
