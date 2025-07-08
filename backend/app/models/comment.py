import uuid
from datetime import datetime
from app import db

class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    content = db.Column(db.Text, nullable=False)
    is_approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 外部キー
    user_id = db.Column(db.String(36), db.ForeignKey('users.user_id'), nullable=False)
    post_id = db.Column(db.String(36), db.ForeignKey('posts.post_id'), nullable=False)

    # リレーションシップ
    user = db.relationship('User', backref='comments')

    def __repr__(self):
        return f'<Comment {self.comment_id}>'