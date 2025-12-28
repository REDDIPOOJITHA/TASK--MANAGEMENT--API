from flask import Blueprint
from src.controllers.task_controller import fetch_tasks, add_task

task_bp = Blueprint('task_bp', __name__)

task_bp.route('/', methods=['GET'])(fetch_tasks)
task_bp.route('/', methods=['POST'])(add_task)
