import flask

app = flask.Flask(__name__)


def string_has_uppercase(query):
    return True if any(letter.isupper() for letter in query) else False


def string_has_lowercase(query):
    return True if any(letter.islower() for letter in query) else False


def string_has_number(query):
    return True if any(letter.isdigit() for letter in query) else False


def string_has_special_chars(query):
    return True if any(not letter.isalnum() for letter in query) else False


@app.route('/string/<query>', methods=['GET'])
def rev(query):
    result = {
        "hasUpper": string_has_uppercase(query),
        "hasLower": string_has_lowercase(query),
        "hasNumber": string_has_number(query),
        "hasSpecial": string_has_special_chars(query)
    }
    return result


app.run()
