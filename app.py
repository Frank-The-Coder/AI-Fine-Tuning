from flask import Flask, render_template, jsonify, request
import openai
import os

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json['message']
    
    # Use the new chat completion format
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4" if your API key has access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=150  # Adjust this value based on your needs
    )
    
    # Get the reply from the assistant
    reply = response['choices'][0]['message']['content'].strip()
    
    return jsonify(reply=reply)

if __name__ == '__main__':
    app.run(debug=True)
