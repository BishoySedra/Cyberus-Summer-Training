from flask import Flask
import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

create = '''
    CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    score INTEGER)
'''



cursor.execute(create)

insert = '''
    INSERT INTO users(username, score) values ("bishoy", 100)
'''
cursor.execute(insert)

select = '''
    select * from users
'''

cursor.execute(select)
connection.commit()

arr = cursor.fetchall()
print(arr)

