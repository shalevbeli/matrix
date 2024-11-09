import pytest
from app import app

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

# Test for the '/api/data' route (GET request)
def test_get_data(client, mocker):
    mocker.patch('server.db["mycollection"].find', return_value=[{"name": "Alice"}, {"name": "Bob"}])
    
    response = client.get('/api/data')
    data = response.get_json()
    
    assert response.status_code == 200
    assert isinstance(data, list)  # Data should be a list
    assert len(data) == 2  # Two documents are returned from the mock
    assert data[0]['name'] == "Alice"
    assert data[1]['name'] == "Bob"

# Test for '/api/data' route failure (e.g., when MongoDB is down)
def test_get_data_failure(client, mocker):
    # Mock MongoDB to raise an exception
    mocker.patch('server.db["mycollection"].find', side_effect=Exception('MongoDB connection error'))
    
    response = client.get('/api/data')
    data = response.get_json()
    
    assert response.status_code == 500
    assert 'error' in data
    assert data['error'] == "MongoDB connection error"