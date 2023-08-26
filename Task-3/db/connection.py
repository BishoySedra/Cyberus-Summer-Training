import sqlite3

from helpers.hashing import *


def connectDB():
    return sqlite3.connect("db/database.db")


def init_db():
    connection = connectDB()

    users_table = """
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        )"""

    gadgets_table = """
        CREATE TABLE IF NOT EXISTS gadgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            image_url TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )"""

    comments_table = """
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gadget_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (gadget_id) REFERENCES gadgets (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """

    cursor = connection.cursor()

    # creating tables execution
    cursor.execute(users_table)
    cursor.execute(gadgets_table)
    cursor.execute(comments_table)

    connection.commit()


def add_user(username, password):
    connection = connectDB()

    addingQuery = f"""
        INSERT INTO users(username, password) VALUES(?, ?)
        """

    cursor = connection.cursor()

    cursor.execute(addingQuery, (username, hash_password(password)))

    connection.commit()


def get_all_users():
    connection = connectDB()

    gettingQuery = f"""
        SELECT * FROM users
        """

    cursor = connection.cursor()

    cursor.execute(gettingQuery)

    return cursor.fetchall()


def get_user_by_username(username):
    connection = connectDB()

    gettingQuery = f"""
        SELECT * FROM users WHERE username = ?
        """

    cursor = connection.cursor()

    cursor.execute(gettingQuery, (username,))

    return cursor.fetchone()


def get_user(username, password):
    connection = connectDB()

    gettingQuery = f"""
        SELECT * FROM users WHERE username = ? AND password = ?
        """

    cursor = connection.cursor()

    cursor.execute(gettingQuery, (username, hash_password(password)))

    return cursor.fetchall()


def add_gadget(user_id, title, description, price, image_url=None):
    connection = connectDB()
    cursor = connection.cursor()
    query = """INSERT INTO gadgets (user_id, title, description, price, image_url) VALUES (?, ?, ?, ?, ?)"""
    cursor.execute(query, (user_id, title, description, price, image_url))
    connection.commit()


def get_gadget(gadget_id):
    connection = connectDB()
    cursor = connection.cursor()
    query = """SELECT * FROM gadgets WHERE id = ?"""
    cursor.execute(query, (gadget_id,))
    return cursor.fetchone()


def get_user_gadgets(user_id):
    connection = connectDB()
    cursor = connection.cursor()
    query = """SELECT * FROM gadgets WHERE user_id = ?"""
    cursor.execute(query, (user_id,))
    return cursor.fetchall()


def get_all_gadgets():
    connection = connectDB()
    cursor = connection.cursor()
    query = """SELECT * FROM gadgets"""
    cursor.execute(query)
    return cursor.fetchall()


def add_comment(gadget_id, user_id, text):
    connection = connectDB()
    cursor = connection.cursor()
    query = """INSERT INTO comments (gadget_id, user_id, text) VALUES (?, ?, ?)"""
    cursor.execute(query, (gadget_id, user_id, text))
    connection.commit()


def get_comments_for_gadget(gadget_id):
    connection = connectDB()
    cursor = connection.cursor()
    query = """
        SELECT  users.username, comments.text, comments.timestamp
        FROM comments
        JOIN users ON comments.user_id = users.id
        WHERE comments.gadget_id = ?
    """
    cursor.execute(query, (gadget_id,))
    return cursor.fetchall()
