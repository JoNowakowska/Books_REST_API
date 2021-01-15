from flask_restful import Resource


class Book(Resource):
    def get(self):
        pass


class BookID(Resource):
    def get(self, book_id):
        pass
