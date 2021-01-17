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

    book_volume = db.relationship('BookVolume', back_populates="search_info")

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()