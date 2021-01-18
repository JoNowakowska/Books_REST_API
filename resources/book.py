from flask_restful import Resource
from flask import request, render_template

from models.book_volume import BookVolume


class Book(Resource):
    def get(self):
        all_book_volumes_list = BookVolume.show_all_book_volumes()
        return render_template('home.html', all_book_volumes_list=all_book_volumes_list)

    def post(self):
        if request.form['submit_button'] == 'FilterByYear':
            print('Hello')

        # published_year = request.args.get('published_date')
        # list_of_authors = request.args.getlist('author')
        # if published_year:
        #    filtered_book_volumes_list = BookVolume.filter_by_year(published_year)


class BookID(Resource):
    def get(self, book_id):
        book_info = BookVolume.show_by_id(book_id)
        return render_template('book.html', book_id=book_id, book_info=book_info)
