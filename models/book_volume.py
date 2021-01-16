from db import db

from datetime import datetime


class BookVolume(db.Model):
    __tablename__ = 'book_volume'
    id = db.Column(db.Integer(), primary_key=True)
    kind = db.Column(db.String(100))
    internal_id = db.Column(db.String(100))
    etag = db.Column(db.String(100))
    selfLink = db.Column(db.String(250))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow())
    last_update = db.Column(db.DateTime(), default=datetime.utcnow())

    volume_info = db.relationship('VolumeInfo')
