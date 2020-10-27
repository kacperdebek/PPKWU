import flask

app = flask.Flask(__name__)


@app.route('/string/', methods=['GET'])
def rev():
    return "Success!"


app.run()
