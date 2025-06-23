from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_and_get_task():
    # Create a task
    response = client.post("/tasks/", json={
        "title": "Test Task",
        "description": "From integration test",
        "completed": False
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"

    # Fetch it back
    task_id = data["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
