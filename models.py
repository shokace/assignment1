from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

# Initialize SQLAlchemy
db = SQLAlchemy()

class Message(db.Model):
    __tablename__ = 'messages'

    message_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chat_id = db.Column(UUID(as_uuid=True), nullable=False)
    content = db.Column(db.String, nullable=False)
    rating = db.Column(db.Boolean, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    role = db.Column(db.Enum('ai', 'user', name='role_enum'), nullable=False)

    def to_dict(self):
        return {
            "message_id": str(self.message_id),
            "chat_id": str(self.chat_id),
            "content": self.content,
            "rating": self.rating,
            "sent_at": self.sent_at.isoformat(),
            "role": self.role
        }