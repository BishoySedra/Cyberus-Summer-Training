from flask import Flask, render_template, request

from db.connection import *

app = Flask(__name__)

@app.route('/add')
def add():
    username = request.args.get("username")
    password = request.args.get("password")

    add_user(username, password)
    
    return "User Successfully Added!"


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        return "Registered!!"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
