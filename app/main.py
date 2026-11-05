
from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary in-memory task storage
tasks = []


# Check whether the API is running
@app.get("/healthz")
def health_check():
    return jsonify({"status": "ok"}), 200


# Retrieve all tasks
@app.get("/tasks")
def get_tasks():
    return jsonify(tasks), 200


# Create a new task
@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not isinstance(data.get("title"), str) or not data["title"].strip():
        return jsonify({"error": "A task title is required"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"].strip(),
        "completed": False
    }

    tasks.append(task)

    return jsonify(task), 201
