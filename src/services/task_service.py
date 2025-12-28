from src.models.task import Task
from src.app import db

def get_all_tasks():
    return Task.query.all()

def create_task(title):
    task = Task(title=title)
    db.session.add(task)
    db.session.commit()
    return task
