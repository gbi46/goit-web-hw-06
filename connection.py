import sqlite3

def create_connection():
    # connect to db
    conn = sqlite3.connect('university.db')

    return conn

