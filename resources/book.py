from flask_restful import Resource
from flask import request, render_template

from models.book_volume import BookVolume


class Book(Resource):
    def get(self):
        published_year = request.args.get('published_date')
        list_of_authors = request.args.getlist('author')
        print(request.args)

        if published_year:
            all_book_volumes_list = BookVolume.filter_by_year(published_year)
            return render_template('home.html', all_book_volumes_list=all_book_volumes_list)
        elif list_of_authors:
            all_book_volumes_list = BookVolume.filter_by_authors(list_of_authors)
            return render_template('home.html', all_book_volumes_list=all_book_volumes_list)
        elif len(request.args) == 0:
            all_book_volumes_list = BookVolume.show_all_book_volumes()
            return render_template('home.html', all_book_volumes_list=all_book_volumes_list)
        else:
            return {"msg": "Not found"}, 404

        # published_year = request.args.get('published_date')
        # list_of_authors = request.args.getlist('author')
        # if published_year:
        #    filtered_book_volumes_list = BookVolume.filter_by_year(published_year)

    def post(self):
        if request.form['submit_button'] == 'FilterByYear':
            print('Hello')



class BookID(Resource):
    def get(self, book_id):
        book_info = BookVolume.show_by_id(book_id)
        return render_template('book.html', book_id=book_id, book_info=book_info)


class Author(Resource):
    def get(self):
        list_of_authors = request.args.getlist('author')
        results = BookVolume.filter_by_authors(list_of_authors)
        return {"msg": results}