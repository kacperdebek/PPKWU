import flask

app = flask.Flask(__name__)


@app.route('/rev/<query>', methods=['GET'])
def rev(query):
    response = {"reversed": query[::-1]}
    return response


app.run()
