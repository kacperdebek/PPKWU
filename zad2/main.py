import flask

app = flask.Flask(__name__)


def string_has_uppercase(query):
    return True if any(letter.isupper() for letter in query) else False


@app.route('/string/<query>', methods=['GET'])
def rev(query):
    return f"Success! Parameter: {query}"


app.run()
