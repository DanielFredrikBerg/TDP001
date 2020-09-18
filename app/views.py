from flask import Flask, jsonify, render_template
from app import app

#app = Flask(__name__, static_folder='app', static_url_path="/app")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('about')
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """


