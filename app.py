from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect

app = Flask(__name__)

bigDictionaryOfMovies = {"movies":
                         [{"id": 1, "name" : "Transformers 1"},
                         {"id" : 2, "name" : "Transformers 2"},
                         {"id" : 3, "name" : "Transformers 3"}]
                         }

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/movies')
def movies():
    return render_template('viewmovies.html')

@app.route('/addmovie', methods= ['POST','GET'])
def addmovie():
    if request.method == 'POST':
        
        return redirect(url_for('index'))
    else:
        return render_template('addmovie.html')
    
@app.route('/games')
def games():
    return render_template('viewmovies.html')

@app.route('/addgame')
def addgame():
    return render_template('viewmovies.html')

with app.test_request_context():
    print(url_for('index'))
    print(url_for('movies'))
    print(url_for('addmovie', movie_name = 'Transform4'))
    print(url_for('games'))
    print(url_for('addgame'))