from app import app 
from app import render_template


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/contatos")
def contatos():
    return "ola lindo"


@app.route("/usuarios/<nome_usuario>")
def usuarios():
    return "ola"