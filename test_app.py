from app import app


def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}
    
def test_create_and_list_task():
    client = app.test_client()
    resp = client.post("/tasks", json={"title": "write tests"})
    assert resp.status_code == 201
    assert resp.get_json()["title"] == "write tests"

    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert len(resp.get_json()) == 1


def test_create_task_missing_title():
    client = app.test_client()
    resp = client.post("/tasks", json={})
    assert resp.status_code == 400