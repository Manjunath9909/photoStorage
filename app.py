from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/api/v1/movies')
def moviesWeDo():
    return {'movies':[{'id': 1, 'name': 'Tramsformers 1'}, {'id': 2, 'name': 'Tramsformers 2'}, {'id': 3, 'name': 'Tramsformers 3'}]}

@app.route('/')
def index():
    return '<center> main page </center>'

@app.route('/api/v1/games')
def games():
    return "doing somethign about games"

@app.route('/api/v1/adverts')
def adverts():
    return "do something about adverts"

@app.route('/api/v1/photoviewer')
def photos():
    return "do somethign about photos"

@app.route('/api/v1/adduser/<int:id>')
def adduser(id):
    if id == 1:
        return f"<center>Hello user {id}</center>"
    elif id == 2:
        return f"<center>Hello user {id}</center>"
    else:
        return f"<center>User {id} not found</center>"
