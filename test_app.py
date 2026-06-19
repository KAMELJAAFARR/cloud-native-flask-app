from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_add_task():
    client = app.test_client()
    response = client.post("/tasks", json={"title": "Test task"})
    assert response.status_code == 201
    assert response.json["title"] == "Test task"