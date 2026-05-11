from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
import os
import markdown as MD

with open('System.txt', 'r') as file:
    System = file.read()

API_KEY = os.environ.get("API_KEY")

Client = genai.Client(api_key=API_KEY)
SearchTool = types.Tool(google_search=types.GoogleSearch())
Configuration = types.GenerateContentConfig(tools=[SearchTool], system_instruction=System)

Web = Flask(__name__)

def Response(Message):
    response = Client.models.generate_content(model="gemini-2.5-flash", config=Configuration, contents=[Message])
    return MD.markdown(response.text)

@Web.route('/')
def index():
    return render_template('index.html')

@Web.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    UserMessage = data.get('message')
    Message = Response(UserMessage)
    return jsonify({'response': Message})

if __name__ == '__main__':
    Web.run(host="0.0.0.0", port=5000)