import sqlite3

def connectDB():
    return sqlite3.connect("data.db")

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

    cursor.execute(addingQuery, (username, password))

    connection.commit()
