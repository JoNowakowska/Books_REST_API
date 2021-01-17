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

    volume_info = db.relationship('VolumeInfo')
    sale_info = db.relationship('SaleInfo')
    access_info = db.relationship('AccessInfo')
    search_info = db.relationship('SearchInfo')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def filter_by_year(cls, published_date):
        #all_volumes = cls.query.join(VolumeInfo).filter(VolumeInfo.publishedDate.like(published_date)).all()
        all_volumes = cls.query.all()
        print(all_volumes)
