import flask

app = flask.Flask(__name__)


@app.route('/rev/<query>', methods=['GET'])
def rev(query):
    return query[::-1]


app.run()
