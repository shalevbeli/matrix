# server.py
import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
import env

app = Flask(__name__)

# MongoDB connection details from environment variables
mongo_host = env.MONGODB_HOST
mongo_port = int(env.MONGODB_PORT)
mongo_user = env.MONGODB_USERNAME
mongo_password = env.MONGODB_PASSWORD
mongo_dbname = env.MONGODB_DBNAME

# Create MongoDB client
mongo_uri = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/"
client = MongoClient(mongo_uri)
db = client[mongo_dbname]  # Connect to the specified database

# Route 1: Example endpoint to fetch a simple message
@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from the server!"})

# Route 2: Example endpoint to process data sent from the client
@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.get_json()
    processed_data = data.get("input_data", "").upper()  # Just an example transformation
    return jsonify({"processed_data": processed_data})

# Route 3: New endpoint to retrieve data from MongoDB
@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # Retrieve all documents from the "mycollection" collection
        collection = db["mycollection"]
        data = collection.find({}, {"_id": 0})  # Retrieve all documents, excluding the '_id' field

        # Convert cursor to a list of dictionaries
        data_list = list(data)
        return jsonify(data_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()