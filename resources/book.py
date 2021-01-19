from flask_restful import Resource
from flask import request

from models.book_volume import BookVolume


class Book(Resource):
    def get(self):
        published_year = request.args.get('published_date')
        list_of_authors = request.args.getlist('author')
        sort_method = request.args.getlist('sort')

        if published_year:
            all_book_volumes_list = BookVolume.filter_by_year(published_year)
            return {
                       "books published in {}".format(published_year): all_book_volumes_list
                   }, 200
        elif list_of_authors:
            all_book_volumes_list = BookVolume.filter_by_authors(list_of_authors)
            return {
                       "books written by {}".format(
                           " or ".join(list_of_authors)
                       ): all_book_volumes_list
                   }, 200
        elif sort_method:
            if sort_method == ['-published_date']:
                all_book_volumes_list = BookVolume.sort_by_published_date_desc()
                return {
                           "books currently saved to db sorted descending": all_book_volumes_list
                       }, 200
            elif sort_method == ['published_date']:
                all_book_volumes_list = BookVolume.sort_by_published_date_asc()
                return {
                           "books currently saved to db sorted ascending": all_book_volumes_list
                       }, 200
            else:
                return {"msg": "URL not found"}, 404
        elif len(request.args) == 0:
            all_book_volumes_list = BookVolume.show_all_book_volumes()
            return {
                       "books currently saved to db": all_book_volumes_list
                   }, 200
        else:
            return {"msg": "URL not found"}, 404


class BookID(Resource):
    def get(self, book_id):
        book_info = BookVolume.show_by_id(book_id)
        return {
                "book with id {}".format(book_id): book_info
                }, 200
