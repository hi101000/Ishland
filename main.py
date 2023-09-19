from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login)
def login():
    return "<p>Hi</p>"

@app.route("/login/<int:id>/<str:psswd>")
def logging_in(id, psswd):
    return "<p>Hola</p>"
