import random, json
import base64
import time

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Index Page: '+ str(time.time())+'</h1>'

@app.route('/chamcong', methods=['POST'])
def chamcong():
	# data = request.get_json()
	# # print(type(data))
	# img = data['image']
	# # print(type(img))
	# img_bytes = base64.b64decode(img)
	# file = open(path + 'img_'+str(time.time())+'.jpeg', 'wb')
	# file.write(img_bytes)
	return "{\"status\":\"OK\"}"
@app.route('/tracuu', methods=['POST'])
def tracuu():
	# data = request.get_json()
	# img = data['image']
	# print(img)
	return "{\"status\":\"OK\"}"

def themanh():
	data = request.get_json()
	img = data['image']
	id_employee = data['id_employee']
	path = '/home/employee_images/' + str(id_employee)
	img_bytes = base64.b64decode(img)
	file = open(path + 'img_'+str(time.time())+'.jpeg', 'wb')
	file.write(img_bytes)

	return "{\"status\":\"OK\"}"