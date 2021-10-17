from flask import Flask, render_template, request, session
from flask_bootstrap import Bootstrap
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("LOGINVISTA.HTML")
    
@app.route("/REGISTROVISTA.HTML")
def reg():
    return render_template("REGISTROVISTA.HTML")

@app.route("/LOGINVISTA.HTML")
def log():
    return render_template("LOGINVISTA.HTML")
    
@app.route("/pagina.html")
def pag():
    return render_template("pagina.html")

@app.route("/CV", methods=["GET", "POST"])
def CV():
    if request.method== "GET":
        return "Please use the form insted."
    name = request.form.get("name")
    name2 = request.form.get("name2")
    name3 = request.form.get("name3")
    name4 = request.form.get("name4")
    name5 = request.form.get("name5")
    name6 = request.form.get("name6")
    name7= request.form.get("name7")
    if not session.get("notes"):
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("CV.html", name=name, name2=name2, name3=name3, name4=name4, name5=name5, name6=name6, name7=name7)


