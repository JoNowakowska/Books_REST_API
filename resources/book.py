from flask_restful import Resource
from flask import request, render_template

from models.book_volume import BookVolume


class Book(Resource):
    def get(self):
        published_year = request.args.get('published_date')
        list_of_authors = request.args.getlist('author')
        sort_method = request.args.getlist('sort')

        if published_year:
            all_book_volumes_list = BookVolume.filter_by_year(published_year)
            return render_template('home.html', all_book_volumes_list=all_book_volumes_list)
        elif list_of_authors:
            all_book_volumes_list = BookVolume.filter_by_authors(list_of_authors)
            return render_template('home.html', all_book_volumes_list=all_book_volumes_list)
        elif sort_method:
            if sort_method == ['-published_date']:
                all_book_volumes_list = BookVolume.sort_by_published_date_desc()
                return render_template('home.html', all_book_volumes_list=all_book_volumes_list)
            elif sort_method == ['published_date']:
                all_book_volumes_list = BookVolume.sort_by_published_date_asc()
                return render_template('home.html', all_book_volumes_list=all_book_volumes_list)
            #else:
                #return {"msg": "URL not found"}, 404
        elif len(request.args) == 0:
            all_book_volumes_list = BookVolume.show_all_book_volumes()
            return render_template('home.html', all_book_volumes_list=all_book_volumes_list)
        #else:
            #return {"msg": "URL not found"}, 404

    #def post(self):
    #    if request.form['FilterByYear'] == 'FilterByYear':
    #        print('Hello')


class BookID(Resource):
    def get(self, book_id):
        book_info = BookVolume.show_by_id(book_id)
        return render_template('book.html', book_id=book_id, book_info=book_info)
