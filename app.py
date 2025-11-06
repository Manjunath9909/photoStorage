from flask import Flask

app = Flask(__name__)

@app.route('/movies')
def moviesWeDo():
    return {'movies':[{'id': 1, 'name': 'Tramsformers 1'}, {'id': 2, 'name': 'Tramsformers 2'}, {'id': 3, 'name': 'Tramsformers 3'}]}
