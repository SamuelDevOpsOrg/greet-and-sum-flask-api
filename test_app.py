import pytest
from app import app

@pytest.fixture
def client():
    """Fixture for setting up the test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Test the hello endpoint."""
    response = client.get('/')
    json_data = response.get_json()
    
    assert response.status_code == 200
    assert json_data['message'] == 'Hello, World!!'

def test_greet(client):
    """Test the greet endpoint."""
    response = client.get('/greet/Samuel')
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data['message'] == 'Hello, Samuel!'

def test_add(client):
    """Test the add endpoint with POST request."""
    response = client.post('/add', json={'a': 2, 'b': 3})
    json_data = response.get_json()
    
    assert response.status_code == 200
    assert json_data['result'] == 5

# def test_add_missing_param(client):
#     """Test the add endpoint with missing parameters."""
#     response = client.post('/add', json={'a': 2})
#     json_data = response.get_json()
        
#     assert response.status_code == 500  # Should return a 500 error due to missing 'b'