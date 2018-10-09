import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Hello, Clarice, KISS MY FACE!'


@app.route('/about')
def about():
    return '<h1>About</h1>'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
