import uuid
from datetime import datetime
from app import db

class Work(db.Model):
    __tablename__ = 'works'

    work_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    project_url = db.Column(db.String(500))
    github_url = db.Column(db.String(500))
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 外部キー
    user_id = db.Column(db.String(36), db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        return f'<Work {self.title}>'
