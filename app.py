from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World in a whole new way!'
	
@app.route('/no')
def no():
	return 'You said no'