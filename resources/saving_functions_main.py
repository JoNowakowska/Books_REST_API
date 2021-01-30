from api_key import API_KEY
from models.book_volume import BookVolume
from resources.saving_finctions_book_volume import save_book_volume
from resources.saving_functions_access_info import save_access_info
from resources.saving_functions_sale_info import save_sale_info
from resources.saving_functions_search_info import save_search_info
from resources.saving_functions_volume_info import save_volume_info

import requests


GOOGLE_BOOKS_API_URL = 'https://www.googleapis.com/books/v1/volumes'


def get_items_from_url(q):
    search_url = GOOGLE_BOOKS_API_URL + '?q={}&key={}'.format(q, API_KEY)
    r = requests.get(search_url)
    items_to_save_to_db = r.json()
    return items_to_save_to_db


def save_items(items_to_save_to_db):
    unsaved_internal_id_list = []

    for item in items_to_save_to_db.get('items'):
        item_internal_id = item.get('id')
        if item_internal_id:
            existing_in_db = BookVolume.find_by_internal_id(item_internal_id)
            if existing_in_db:
                unsaved_internal_id_list.append(item_internal_id)
            else:
                book_volume_item_id = save_book_volume(item)
                if book_volume_item_id:
                    item_volume_info = item.get('volumeInfo')
                    item_sale_info = item.get('saleInfo')
                    item_access_info = item.get('accessInfo')
                    item_search_info = item.get('searchInfo')
                    if item_volume_info:
                        save_volume_info(item_volume_info, book_volume_item_id)
                    if item_sale_info:
                        save_sale_info(item_sale_info, book_volume_item_id)
                    if item_access_info:
                        save_access_info(item_access_info, book_volume_item_id)
                    if item_search_info:
                        save_search_info(item_search_info, book_volume_item_id)

    return unsaved_internal_id_list