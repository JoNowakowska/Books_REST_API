from db import db


class SearchInfo(db.Model):
    __tablename__ = 'search_info'
    id = db.Column(db.Integer(), primary_key=True)
    book_volume_id = db.Column(
        db.Integer(),
        db.ForeignKey('book_volume.id'),
        nullable=False
    )
    textSnippet = db.Column(db.String(500))