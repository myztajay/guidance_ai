from flask import Blueprint, jsonify, render_template, Flask
from openai import OpenAI


client = OpenAI()
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

@app.route('/get_api_data')
def get_api_data():
    my_assistant = client.beta.assistants.create(
        instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
        name="Math Tutor",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-turbo",
    )
    return jsonify(my_assistant)