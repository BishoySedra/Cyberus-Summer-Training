from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from db.connection import *
from helpers.fileUploadRestrictions import *
from helpers.passwordPolicies import *

app = Flask(__name__)
app.secret_key = "password"
limiter = Limiter(
    get_remote_address, app=app, default_limits=["200 per day", "50 per hour"]
)


## Routes


@app.route("/upload", methods=["POST", "GET"])
@limiter.limit("20 per minute")
def uploadGadget():
    if request.method == "GET":
        if "user_id" in session:
            return render_template("upload-gadget.html")
        else:
            flash("You must login first to upload your gadget!", "danger")
            return redirect(url_for("login"))
    else:
        user_id = session["user_id"]
        title = request.form["title"]
        description = request.form["description"]
        price = request.form["price"]
        image = request.files["image"]
        image_url = f"uploads/{image.filename}"
        image.save(f"static/{image_url}")

        if not allowed_file_size(image) or not allowed_file_extension(image.filename):
            flash("Invalid file uploaded!!", "danger")
            return render_template("upload-gadget.html")

        add_gadget(user_id, title, description, price, image_url)

        return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        user = get_user_by_username(username)

        if user:
            flash("Username already exists!", "danger")
            return render_template("register.html")

        if check_password_policies(password):
            add_user(username, password)
            flash("Username is registered Successfully!", "success")
        else:
            flash("Your password is weak try another strong one!", "warning")
            return render_template("register.html")

    return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
@limiter.limit("20 per minute")
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = get_user_by_username(username)

        if user:
            if is_password_matched(password, user[2]):
                session["username"] = user[1]
                session["user_id"] = user[0]
                return redirect(url_for("index"))

        flash("Invalid Credentials!", "danger")
        return render_template("login.html")

    else:
        return render_template("login.html")


@app.route("/")
def index():
    if "username" in session:
        return render_template(
            "index.html", gadgets=get_user_gadgets(session["user_id"])
        )
    else:
        flash("You're not logged in", "danger")
        return redirect(url_for("login"))


## End of Routes

## Begin of running app
if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)
## End of running app
