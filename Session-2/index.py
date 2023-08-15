from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from db.connection import *

app = Flask(__name__)
app.secret_key = "password"
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form['username']
        password = request.form['password']

        user = get_user_by_username(username)

        if(user):
            flash('Username already exists!', "danger")
            return render_template('register.html')
        
        flash('Username is registered Successfully!', "success")
        add_user(username,password)
    return redirect(url_for('login'))

@app.route('/login', methods = ['POST','GET'])
@limiter.limit('5 per minute')
def login():
    if(request.method == 'POST'):

        username = request.form['username']
        password = request.form['password']

        user = get_user_by_username(username)
        
        if(user):
            if is_password_matched(password, user[2]):
                session["username"] = user[1]
                return redirect(url_for('index'))
            
        flash("Invalid Credentials!", "danger")
        return render_template('login.html')
    
    else:
        return render_template('login.html')

@app.route('/')
def index():
    if "username" in session:
        return f'''Hello {session["username"]}!'''
    else:
        return "You're not logged in"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
