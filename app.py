from flask import Blueprint, render_template, Flask


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    return render_template('aboutme.html')

@app.route('/about_app')
def about_app():
    return render_template('aboutapp.html')

@app.route('/get_guidance')
def get_guidance():
    return render_template('getguidance.html')