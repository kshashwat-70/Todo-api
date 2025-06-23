from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Test Desc", "completed": False})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    response = client.post("/tasks/", json={"title": "Update Task", "description": "Test", "completed": False})
    task_id = response.json()["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated", "description": "Updated Desc", "completed": True})
    assert response.status_code == 200
    assert response.json()["completed"] == True

def test_delete_task():
    response = client.post("/tasks/", json={"title": "Delete Task", "description": "Test", "completed": False})
    task_id = response.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"
