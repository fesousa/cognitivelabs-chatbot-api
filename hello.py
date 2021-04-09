from flask import Flask, render_template, request, jsonify
import os
import json
from ibm_watson import AssistantV2

app = Flask(__name__, static_url_path='')

# configuração para CloudFoundry IBM
port = int(os.getenv('PORT', 8000))

@app.route('/')
def home():     
    
    return "<h1>Olá Flask!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
