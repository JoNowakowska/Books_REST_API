from datetime import datetime

from sqlalchemy import text, or_

from db import db

from models.volume_info import VolumeInfo, ImageLinks


class BookVolume(db.Model):
    __tablename__ = 'book_volume'
    id = db.Column(db.Integer(), primary_key=True)
    kind = db.Column(db.String(100))
    internal_id = db.Column(db.String(100)) #, unique=True)
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
    def find_by_internal_id(cls, internal_id):
        book_volume = cls.query.filter_by(internal_id=internal_id).first()
        return book_volume

    @classmethod
    def show_all_book_volumes(cls):
        all_book_volumes = cls.query.join(
            VolumeInfo, BookVolume.id == VolumeInfo.book_volume_id
        ).join(
            ImageLinks, VolumeInfo.imageLinks_id == ImageLinks.id
        ).all()
        all_book_volumes_list = []
        for book_volume in all_book_volumes:
            new_element = {
                "title": book_volume.volume_info.title,
                "authors": book_volume.volume_info.authors,
                "published_date": book_volume.volume_info.publishedDate,
                "categories": book_volume.volume_info.categories,
                "average_rating": book_volume.volume_info.averageRating,
                "ratings_count": book_volume.volume_info.ratingsCount,
                "thumbnail": book_volume.volume_info.image_links.thumbnail
            }
            all_book_volumes_list.append(new_element)
        return all_book_volumes_list

    @classmethod
    def show_by_id(cls, book_id):
        book = BookVolume.query.join(
            VolumeInfo, BookVolume.id == VolumeInfo.book_volume_id
        ).join(
            ImageLinks, VolumeInfo.imageLinks_id == ImageLinks.id
        ).filter(
            BookVolume.id == book_id
        ).first()
        book_info = {
            "title": book.volume_info.title,
            "authors": book.volume_info.authors,
            "published_date": book.volume_info.publishedDate,
            "categories": book.volume_info.categories,
            "average_rating": book.volume_info.averageRating,
            "ratings_count": book.volume_info.ratingsCount,
            "thumbnail": book.volume_info.image_links.thumbnail
        }
        return book_info

    @classmethod
    def filter_by_year(cls, published_year):
        filtered_book_volumes = cls.query.join(
            VolumeInfo, BookVolume.id == VolumeInfo.book_volume_id
        ).join(
            ImageLinks, VolumeInfo.imageLinks_id == ImageLinks.id
        ).filter(
            VolumeInfo.publishedDate.contains(published_year)
        ).all()
        filtered_book_volumes_list = []
        for book_volume in filtered_book_volumes:
            new_element = {
                "title": book_volume.volume_info.title,
                "authors": book_volume.volume_info.authors,
                "published_date": book_volume.volume_info.publishedDate,
                "categories": book_volume.volume_info.categories,
                "average_rating": book_volume.volume_info.averageRating,
                "ratings_count": book_volume.volume_info.ratingsCount,
                "thumbnail": book_volume.volume_info.image_links.thumbnail
            }
            filtered_book_volumes_list.append(new_element)
        return filtered_book_volumes_list

    @classmethod
    def sort_by_published_date_asc(cls):
        all_book_volumes = cls.query.join(
            VolumeInfo, BookVolume.id == VolumeInfo.book_volume_id
        ).join(
            ImageLinks, VolumeInfo.imageLinks_id == ImageLinks.id
        ).order_by(
            VolumeInfo.publishedDate
        ).all()
        all_book_volumes_list = []
        for book_volume in all_book_volumes:
            new_element = {
                "title": book_volume.volume_info.title,
                "authors": book_volume.volume_info.authors,
                "published_date": book_volume.volume_info.publishedDate,
                "categories": book_volume.volume_info.categories,
                "average_rating": book_volume.volume_info.averageRating,
                "ratings_count": book_volume.volume_info.ratingsCount,
                "thumbnail": book_volume.volume_info.image_links.thumbnail
            }
            all_book_volumes_list.append(new_element)
        return all_book_volumes_list

    @classmethod
    def sort_by_published_date_desc(cls):
        all_book_volumes = cls.query.join(
            VolumeInfo, BookVolume.id == VolumeInfo.book_volume_id
        ).join(
            ImageLinks, VolumeInfo.imageLinks_id == ImageLinks.id
        ).order_by(
            VolumeInfo.publishedDate.desc()
        ).all()
        all_book_volumes_list = []
        for book_volume in all_book_volumes:
            new_element = {
                "title": book_volume.volume_info.title,
                "authors": book_volume.volume_info.authors,
                "published_date": book_volume.volume_info.publishedDate,
                "categories": book_volume.volume_info.categories,
                "average_rating": book_volume.volume_info.averageRating,
                "ratings_count": book_volume.volume_info.ratingsCount,
                "thumbnail": book_volume.volume_info.image_links.thumbnail
            }
            all_book_volumes_list.append(new_element)
        return all_book_volumes_list

    @classmethod
    def filter_by_authors(cls, author_list):
        filtered_book_volumes_list = []
        for author in author_list:
            filtered_book_volumes = cls.query.join(
                VolumeInfo, BookVolume.id == VolumeInfo.book_volume_id
            ).join(
                ImageLinks, VolumeInfo.imageLinks_id == ImageLinks.id
            ).filter(
                VolumeInfo.authors.contains(author)
            ).all()

            for book_volume in filtered_book_volumes:
                new_element = {
                    "title": book_volume.volume_info.title,
                    "authors": book_volume.volume_info.authors,
                    "published_date": book_volume.volume_info.publishedDate,
                    "categories": book_volume.volume_info.categories,
                    "average_rating": book_volume.volume_info.averageRating,
                    "ratings_count": book_volume.volume_info.ratingsCount,
                    "thumbnail": book_volume.volume_info.image_links.thumbnail
                }
                filtered_book_volumes_list.append(new_element)
        return filtered_book_volumes_list
