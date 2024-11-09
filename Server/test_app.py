import pytest
from app import app
from flask import Flask

# Fixture to set up the Flask app for testing
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test for the '/api/message' route
def test_get_message(client):
    response = client.get('/api/message')
    data = response.get_json()
    
    assert response.status_code == 200
    assert 'message' in data
    assert data['message'] == "Hello from the server!"

# Test for the '/api/process' route (POST request)
def test_process_data(client):
    test_data = {"input_data": "hello"}
    response = client.post('/api/process', json=test_data)
    data = response.get_json()
    
    assert response.status_code == 200
    assert 'processed_data' in data
    assert data['processed_data'] == "HELLO"  # Input data should be transformed to uppercase