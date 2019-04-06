from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'
	
@app.route('/yes')
def yes():
	return 'You said yes!!!'
	
@app.route('/no')
def no():
	return 'You said no'
