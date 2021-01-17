from flask_restful import Resource
from flask import request

from models.book_volume import BookVolume


class Book(Resource):
    def get(self):
        published_date = request.args.get('published_date')
        print(published_date)
        BookVolume.filter_by_year(published_date)


        list_of_authors = request.args.getlist('author')

        return {'published_date': published_date,
                'list_of_authors': list_of_authors}


class BookID(Resource):
    def get(self, book_id):
        return {'book_id': book_id}
