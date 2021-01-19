import os

from db import db

from flask import Flask
from flask_restful import Api

from resources.book import Book, BookID
from resources.book_db import Db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Book, '/books')
api.add_resource(BookID, '/books/<int:book_id>')
api.add_resource(Db, '/db')

db.init_app(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)