from flask import Flask, request
from flask import render_template_string
import hashlib

app = Flask(__name__)

# hash in hex : message as string
hash_map = {}

@app.route('/')
def index():
	return "Hello!"


@app.route('/messages')
def get_messages():
	return hash_map

@app.route('/messages/<hash>')
def get_message(hash):
	value = hash_map.get(hash)
	if value is None:
		return render_template_string('PageNotFound {{ errorCode }}', errorCode='404'), 404
	else:
		return value


@app.route('/messages', methods=['POST'])
def add_message():
	message = request.json['message']
	hash_value = hashlib.sha256(message.encode('utf-8')).hexdigest()
	hash_map[hash_value] = message
	return hash_value