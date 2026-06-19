from app import app

def test_full_workflow():
    client = app.test_client()

    response = client.post("/tasks", json={"title": "Integration Test"})
    assert response.status_code == 201

    response = client.get("/tasks")
    assert response.status_code == 200

    tasks = response.get_json()
    assert len(tasks) > 0