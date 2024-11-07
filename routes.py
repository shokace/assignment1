from flask import Blueprint, request, jsonify
from models import db, Message
from uuid import UUID

messages_bp = Blueprint("messages", __name__)

#POST#
@messages_bp.route("/messages", methods=["POST"])
def create_message():
    data = request.get_json()

    required_fields = ["chat_id", "content", "rating", "sent_at", "role"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    message = Message(
        chat_id=UUID(data["chat_id"]),
        content=data["content"],
        rating=data["rating"],
        sent_at=data["sent_at"],
        role=data["role"],
    )
    db.session.add(message)
    db.session.commit()

    return jsonify(message.to_dict()), 201

#PUT#
@messages_bp.route("/messages/<message_id>", methods=["PUT"])
def update_message(message_id):
    data = request.get_json()

    message = Message.query.get(message_id)
    if message is None:
        return jsonify({"error": "Message not found"}), 404

    if "chat_id" in data:
        message.chat_id = UUID(data["chat_id"])
    if "content" in data:
        message.content = data["content"]
    if "rating" in data:
        message.rating = data["rating"]
    if "sent_at" in data:
        message.sent_at = data["sent_at"]
    if "role" in data:
        message.role = data["role"]

    db.session.commit()
    return jsonify(message.to_dict()), 200

#GET#
@messages_bp.route("/messages", methods=["GET"])
def get_all_messages():
    messages = Message.query.all()
    return jsonify([message.to_dict() for message in messages]), 200
