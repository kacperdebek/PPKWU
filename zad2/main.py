import flask

app = flask.Flask(__name__)


@app.route('/string/<query>', methods=['GET'])
def rev(query):
    return f"Success! Parameter: {query}"


app.run()
