"""
Get the 'GOOGLE_BOOKS_API_KEY' variable from the os environment variables and set it as API_KEY.

To create your own API key, go to Google Books API documentation (https://developers.google.com/books/docs/v1/using)
and follow the guidelines. Then, add the API key as an os environment variable named 'GOOGLE_BOOKS_API_KEY'.
"""

import os

API_KEY = os.environ.get('GOOGLE_BOOKS_API_KEY')
