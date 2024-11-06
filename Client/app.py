# client.py
import os
import requests
from dotenv import load_dotenv
import time

# Load environment variables from the .env file
load_dotenv()

# Read configuration from environment variables
server_url = os.getenv("SERVER_URL", "http://localhost:5000/api")

# Function to get a message from the server
def get_message():
    response = requests.get(f"{server_url}/message")
    if response.status_code == 200:
        print("Server message:", response.json()["message"])
    else:
        print("Failed to get message from server")

# Function to send data to the server and get processed data
def send_data(input_data):
    response = requests.post(f"{server_url}/process", json={"input_data": input_data})
    if response.status_code == 200:
        print("Processed data from server:", response.json()["processed_data"])
    else:
        print("Failed to process data on server")

if __name__ == "__main__":
    while True:
        get_message()
        send_data("hello world")
        time.sleep("30")