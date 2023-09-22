from flask import Flask, render_template, redirect, request, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def main_page():
    return redirect("/index")

@app.route("/index")
def index(auth = False, uname = None):
    return render_template("index.html", login = auth, user = uname)

@app.route("/contact")
def contact(auth = False):
    global logged_in
    return render_template("contact.html", login = auth)

@app.route("/login")
def login():
    return render_template("login.html", login = False)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/authenticate", methods=['POST'])
def authenticate():
    conn = sqlite3.connect('users.db')
    auth = False
    cursor = conn.execute("SELECT id, psswd, email from USERS")
    for row in cursor:
        if (str(row[0]) == request.form.get("uname") or row[2]==request.form.get("uname").lower()) and row[1] == request.form.get("psswd"):
            auth = True
            name = request.form.get("uname")
            conn.close()
            return redirect(url_for(".index", login = auth, uname = name)) #render_template("index.html", login = auth)
    conn.close()
    return render_template("login.html", login="FAILED")

app.run(host="0.0.0.0", port=5001)