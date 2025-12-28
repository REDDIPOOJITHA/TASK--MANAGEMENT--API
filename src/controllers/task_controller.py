from flask import jsonify, request
from src.services.task_service import get_all_tasks, create_task

def fetch_tasks():
    tasks = get_all_tasks()
    return jsonify([{'id': t.id, 'title': t.title} for t in tasks])

def add_task():
    data = request.get_json()
    task = create_task(data['title'])
    return jsonify({'id': task.id, 'title': task.title}), 201
