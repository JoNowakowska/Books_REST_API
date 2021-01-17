import os

from flask import Flask
from flask_restful import Api

from db import db
from resources.book import Book, BookID
from resources.book_db import Db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Book, '/book')
api.add_resource(BookID, '/book/<int:book_id>')
api.add_resource(Db, '/db')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)