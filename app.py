from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, GitHub session folk!'

@app.route('/<a>/add/<b>')
def add(a, b):
    return str(int(a) + int(b))

@app.route('/<a>/minus/<b>')
def minus(a, b):
    return str(int(a) - int(b))
