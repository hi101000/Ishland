from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)

loggen_in = False
uname = None

@app.route("/")
def main_page():
    return redirect("/index")

@app.route("/index")
def index():
    global logged_in
    global uname
    return render_template("index.html", login = logged_in, user = uname)

@app.route("/contact")
def contact():
    global logged_in
    return render_template("contact.html", login = logged_in)

@app.route("/login")
def login():
    return render_template("login.html")

app.run(host="0.0.0.0", port=5001)