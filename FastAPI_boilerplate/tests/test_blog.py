from fastapi.testclient import TestClient
from ..main import app
from ..hashing import Hash
 
client = TestClient(app)
 
 
 
 
def get_auth_headers():
    username = "adi@email"
    password = "adi@password"
    response = client.post(
        "/login",
        data={"username": username, "password": password}
    )
    assert response.status_code == 200
    access_token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    return headers
 
 
def test_read_all():
    headers = get_auth_headers()
    response = client.get("/blog/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
 
 
def test_create():
    headers = get_auth_headers()
    request_payload = {
        "title": "Test Blog",
        "body": "This is a test blog."
    }
    response = client.post("/blog/", json=request_payload, headers=headers)
    assert response.status_code == 201
    assert response.json()["title"] == "Test Blog"
 
 
def test_update():
    headers = get_auth_headers()
    request_payload = {
        "title": "Updated Blog",
        "body": "This is an updated blog."
    }
    response = client.put("/blog/1", json=request_payload, headers=headers)
    assert response.status_code == 202
    assert response.json()["message"] == "Update Successful"
 
 
def test_read_one():
    headers = get_auth_headers()
    response = client.get("/blog/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Blog"
 
 
def test_delete():
    headers = get_auth_headers()
    response = client.delete("/blog/11", headers=headers)
    assert response.status_code == 204
 