# app.py
from flask import Flask
import os

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def index():
    return "Welcome to the Chauffeur Scheduler App!"


if __name__ == '__main__':
    app.run(debug=True)