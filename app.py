from flask import Flask, request
import hashlib

app = Flask(__name__)

# hash map as hex:message
messages = {}

@app.route('/')
def index():
    return "Hello!"

@app.route('/messages')
def get_messages():
    return messages

@app.route('/messages', methods=['POST'])
def add_message():
    # Get the message from the request
    message = request.json['message']
    # Generate the hash of the message
    message_hash = hashlib.sha256(message.encode('utf-8')).hexdigest()

    # Store the message with its hash as the key
    messages[message_hash] = message

    # Return the hash of the message
    return message_hash

@app.route('/messages/<hash>', methods=['GET'])
def get_message(hash):
    # Check if the hash exists in the messages dictionary
    if hash in messages:
        # If it exists, return the message
        return messages[hash]
    else:
        # If it does not exist, return a 404 error
        return 'Error: Message not found', 404

if __name__ == '__main__':
    app.run()
