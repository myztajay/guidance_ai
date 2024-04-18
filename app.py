from flask import Blueprint, jsonify, render_template, Flask
from openai import OpenAI
from secret import OPENAI_API_KEY
import pdb; 



client = OpenAI(api_key=OPENAI_API_KEY)

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

    # assistant = client.beta.assistants.create(
    #     instructions="You are a jesus. When asked a question, write me a humorous response with bible references.",
    #     name="jesus",
    #     tools=[{"type": "code_interpreter"}],
    #     model="gpt-4-turbo",
    # )
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="why am i here?"
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        # test asst
        assistant_id="asst_goGuCjkF11uyVbK95FA3DxpS",
        instructions="You are a jesus. When asked a question, write me a humorous response with bible references."
    )

    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        print(messages)
    else:
        print(run.status)
    # pdb.set_trace()
    res = {
        "message": messages.data[0].content[0].text.value
    }
    print(jsonify(res))
    return jsonify(res)
    # pdb.set_trace()
    
   
    