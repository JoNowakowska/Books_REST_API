from db import db

from datetime import datetime

from models.volume_info import VolumeInfo


class BookVolume(db.Model):
    __tablename__ = 'book_volume'
    id = db.Column(db.Integer(), primary_key=True)
    kind = db.Column(db.String(100))
    internal_id = db.Column(db.String(100))
    etag = db.Column(db.String(100))
    selfLink = db.Column(db.String(250))
    created_at = db.Column(db.DateTime())
    last_update = db.Column(db.DateTime(), default=datetime.utcnow())

    volume_info = db.relationship('VolumeInfo', uselist=False, back_populates="book_volume")
    sale_info = db.relationship('SaleInfo', uselist=False, back_populates="book_volume")
    access_info = db.relationship('AccessInfo', uselist=False, back_populates="book_volume")
    search_info = db.relationship('SearchInfo', uselist=False, back_populates="book_volume")

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def filter_by_year(cls, published_date):
        filtered_book_volumes = cls.query.join(VolumeInfo).filter(
            VolumeInfo.publishedDate.contains(published_date)).all()
        filtered_book_volumes_list = []
        for book_volume in filtered_book_volumes:
            new_element = {"Published date": book_volume.volume_info.publishedDate,
                           "Title": book_volume.volume_info.title}
            filtered_book_volumes_list.append(new_element)
        return filtered_book_volumes_list

    @classmethod
    def sort_by_published_date(cls):
