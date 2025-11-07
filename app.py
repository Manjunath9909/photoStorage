from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
import json

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/movies')
def movies():
    with open("movies.json", "r") as file:
        bigDictionaryOfMovies = json.load(file)
    return render_template('viewmovies.html', movies = bigDictionaryOfMovies)

@app.route('/addmovie', methods= ['POST','GET'])
def addmovie():
    if request.method == 'POST':
        with open("movies.json", "r") as file:
            bigDictionaryOfMovies = json.load(file)
        len = bigDictionaryOfMovies['movieList'].__len__()
        bigDictionaryOfMovies['movieList'].append({"id" : len + 1, "name" : request.form['movie']})
        with open("movies.json", "w") as file:
            json.dump(bigDictionaryOfMovies, file, indent=2)
            
        return redirect(url_for('index'))
    else:
        return render_template('addmovie.html')
    
@app.route('/games')
def games():

    return render_template('viewmovies.html')

@app.route('/addgame')
def addgame():
    return render_template('viewmovies.html')

#with app.test_request_context():
    print(url_for('index'))
    print(url_for('movies'))
    print(url_for('addmovie', movie_name = 'Transform4'))
    print(url_for('games'))
    print(url_for('addgame'))