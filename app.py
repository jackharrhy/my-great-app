from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, GitHub session folk!'

@app.route('/<a>/plus/<b>')
def plus(a, b):
    return str(int(a) - int(b))
