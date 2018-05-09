"""Our main flask app."""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    """Say Hello."""
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
