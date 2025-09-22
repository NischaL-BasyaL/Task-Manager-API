from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models import Task
from werkzeug.exceptions import NotFound, BadRequest

task_bp = Blueprint("task_bp", __name__, url_prefix="/api/tasks")


@task_bp.route("/", methods=["GET"])
@jwt_required()
def list_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).order_by(
        Task.created_at.desc()).all()
    output = []
    for t in tasks:
        output.append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "completed": t.completed,
            "created_at": t.created_at.isoformat()
        })
    return jsonify(output), 200


@task_bp.route("/", methods=["POST"])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    title = data.get("title")
    if not title:
        raise BadRequest("title is required")
    description = data.get("description", "")
    task = Task(title=title, description=description, user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "task created", "id": task.id}), 201


@task_bp.route("/<int:task_id>", methods=["GET"])
@jwt_required()
def get_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        raise NotFound("task not found")
    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": task.created_at.isoformat()
    }), 200


@task_bp.route("/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        raise NotFound("task not found")
    data = request.get_json() or {}
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    if "completed" in data:
        task.completed = bool(data.get("completed"))
    db.session.commit()
    return jsonify({"message": "task updated"}), 200


@task_bp.route("/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        raise NotFound("task not found")
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "task deleted"}), 200
