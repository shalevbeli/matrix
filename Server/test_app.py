# server/test_app.py
import os
import pytest
from app import app

@pytest.fixture
def client():
    os.environ['FLASK_ENV'] = 'testing'
    app = create_app()
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route"""
    response = client.get('/')
    assert response.status_code == 200

def test_api_message(client):
    """Test the API endpoint for messages"""
    response = client.get('/api/message')
    assert response.status_code == 200
    assert response.json['message'] == "Hello from the server!"