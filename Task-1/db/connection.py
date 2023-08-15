import sqlite3

from helpers.hashing import *


def connectDB():
    return sqlite3.connect("database.db")

def init_db():
    connection = connectDB()

    createQuery = '''
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        )'''
    
    cursor = connection.cursor()

    cursor.execute(createQuery)

    connection.commit()

def add_user(username, password):
    connection = connectDB()

    addingQuery = f'''
        INSERT INTO users(username, password) VALUES(?, ?)
        '''
    
    cursor = connection.cursor()

    cursor.execute(addingQuery, (username, hash_password(password)))

    connection.commit()

def get_all():
    connection = connectDB()

    gettingQuery = f'''
        SELECT * FROM users
        '''
    
    cursor = connection.cursor()

    cursor.execute(gettingQuery)

    return cursor.fetchall()

def get_user_by_username(username):
    connection = connectDB()

    gettingQuery = f'''
        SELECT * FROM users WHERE username = ?
        '''
    
    cursor = connection.cursor()

    cursor.execute(gettingQuery,(username,))

    return cursor.fetchone()

def get_user(username, password):
    connection = connectDB()

    gettingQuery = f'''
        SELECT * FROM users WHERE username = ? AND password = ?
        '''
    
    cursor = connection.cursor()

    cursor.execute(gettingQuery,(username,hash_password(password)))

    return cursor.fetchall()

