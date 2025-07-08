import uuid
from app import db

class Tag(db.Model):
    __tablename__ = 'tags'

    tag_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), unique=True, nullable=False)
    slug = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Tag {self.name}>'

# 中間テーブル
post_tags = db.Table('post_tags',
    db.Column('post_id', db.String(36), db.ForeignKey('posts.post_id'), primary_key=True),
    db.Column('tag_id', db.String(36), db.ForeignKey('tags.tag_id'), primary_key=True)
)