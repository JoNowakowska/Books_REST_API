from flask_restful import Resource
from flask import request

from models.book_volume import BookVolume


class Book(Resource):
    def get(self):
        published_date = request.args.get('published_date')
        list_of_authors = request.args.getlist('author')
        if published_date:
            filtered_book_volumes_list = BookVolume.filter_by_year(published_date)
            return {'published_date': published_date,
                    'list_of_book_volumes': filtered_book_volumes_list}

        if list_of_authors:
            pass





class BookID(Resource):
    def get(self, book_id):
        return {'book_id': book_id}
