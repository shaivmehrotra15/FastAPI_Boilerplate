from fastapi.testclient import TestClient
from ..main import app
from ..database import get_db
from .. import models, schemas
 
client = TestClient(app)
 
 
def test_create_user():
    with TestClient(app) as client:
        request_payload = {
            "name": "John Doe",
            "email": "john@example.com",
            "password": "password123"
        }
        response = client.post("/user/", json=request_payload)
        assert response.status_code == 200
        assert response.json()["name"] == "John Doe"
        assert response.json()["email"] == "john@example.com"
 
 
def test_get_user():
    with TestClient(app) as client:
        # Create a user
        request_payload = {
            "name": "John Doe",
            "email": "john@example.com",
            "password": "password123"
        }
        response = client.post("/user/", json=request_payload)
        assert response.status_code == 200
        user_id = response.json()["id"]
 
        # Retrieve the created user
        response = client.get(f"/user/{user_id}")
        assert response.status_code == 200
        assert response.json()["id"] == user_id
        assert response.json()["name"] == "John Doe"
        assert response.json()["email"] == "john@example.com"
 