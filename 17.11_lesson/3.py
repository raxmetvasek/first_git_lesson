from flask import Flask, jsonify, request
import time
import random
app = Flask(__name__)
@app.route('/')
def index():
	return '<h1> Привет от синхронного сервера! </h1>'
@app.route('/api/data')
def get_data():
	time.sleep(2)
	return jsonify({
		'message' : 'Данные получены',
		'value' : random.randint(1,100)
		})
@app.route('/api/echo', methods = ['POST'])
def echo():
	data = request.get_json()
	return jsonify({'recieved' : data})
if __name__=='__main__':
	app.run(debug=True, port = 5000)
