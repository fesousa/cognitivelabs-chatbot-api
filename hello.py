from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__, static_url_path='')

# configuração para CloudFoundry IBM
port = int(os.getenv('PORT', 8000))

@app.route('/dados', methods=['GET', 'POST'])
def dados():         
    return "<h1>Outro endpoint</h1>"

@app.route('/')
def home():         
    return "<h1>Olá Flask!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
