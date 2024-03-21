from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

@app.route('/about')
def about():
    return '<h1>about </h1>'

@app.route('/get_guidance')
def get_guidance():
    return '<h1>about </h1>'