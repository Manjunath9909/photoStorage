from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

bigDictionaryOfMovies = {'movies':[{"Tramsformers 1", "Transformers 2", "Traosformers 4"}]}

@app.route('/')
def index():
    #return render_template('index.html')
    return bigDictionaryOfMovies['movies']

@app.route('/movies')
def movies():
    return render_template('viewmovies.html')

@app.route('/addmovie')
def addmovie():
    return render_template('addmovie.html')

@app.route('/games')
def games():
    return render_template('viewmovies.html')

@app.route('/addgame')
def addgame():
    return render_template('viewmovies.html')