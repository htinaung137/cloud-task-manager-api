
from flask import Flask, jsonify, request
from psycopg import Error

from .database import get_connection

app = Flask(__name__)


# Check application and database health
@app.get("/healthz")
def health_check():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")

        return jsonify({
            "status": "ok",
            "database": "ok"
        }), 200

    except Error:
        return jsonify({
            "status": "error",
            "database": "unavailable"
        }), 503


# Retrieve all tasks from PostgreSQL
@app.get("/tasks")
def get_tasks():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, title, completed "
                "FROM tasks ORDER BY id;"
            )
            tasks = cur.fetchall()

    return jsonify(tasks), 200


# Create a new task in PostgreSQL
@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True)

    if (
        not isinstance(data, dict)
        or not isinstance(data.get("title"), str)
        or not data["title"].strip()
    ):
        return jsonify({
            "error": "A task title is required"
        }), 400

    title = data["title"].strip()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO tasks (title)
                VALUES (%s)
                RETURNING id, title, completed;
                """,
                (title,)
            )
            task = cur.fetchone()

    return jsonify(task), 201

from flask import Flask, jsonify, request
from psycopg import Error

from .database import get_connection

app = Flask(__name__)


# Check application and database health
@app.get("/healthz")
def health_check():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")

        return jsonify({
            "status": "ok",
            "database": "ok"
        }), 200

    except Error:
        return jsonify({
            "status": "error",
            "database": "unavailable"
        }), 503


# Retrieve all tasks from PostgreSQL
@app.get("/tasks")
def get_tasks():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, title, completed "
                "FROM tasks ORDER BY id;"
            )
            tasks = cur.fetchall()

    return jsonify(tasks), 200


# Create a new task in PostgreSQL
@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True)

    if (
        not isinstance(data, dict)
        or not isinstance(data.get("title"), str)
        or not data["title"].strip()
    ):
        return jsonify({
            "error": "A task title is required"
        }), 400

    title = data["title"].strip()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO tasks (title)
                VALUES (%s)
                RETURNING id, title, completed;
                """,
                (title,)
            )
            task = cur.fetchone()

    return jsonify(task), 201
