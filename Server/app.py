# server.py
import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Read configuration from environment variables
app = Flask(__name__)
host = os.getenv("FLASK_HOST", "0.0.0.0")
port = int(os.getenv("FLASK_PORT", 5000))
debug = os.getenv("FLASK_DEBUG", "False").lower() == "true"

# Example endpoint to fetch a simple message
@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from the server!"})

# Example endpoint to process data sent from the client
@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.get_json()
    processed_data = data.get("input_data", "").upper()  # Just an example transformation
    return jsonify({"processed_data": processed_data})

if __name__ == '__main__':
    app.run(debug=debug, host=host, port=port)