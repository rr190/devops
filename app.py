from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []
next_id = 1

@app.get("/tasks")
def list_tasks():
    return jsonify(tasks), 200

@app.get("/health")
def health():
    return jsonify(status = "ok"), 200

@app.post("/tasks")
def create_task():
    global next_id
    data = request.get_json(force=True)
    title = data.get("title")
    if not title:
        return jsonify(error="title is required"), 400
    task = {"id": next_id, "title": title, "done": False}
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
