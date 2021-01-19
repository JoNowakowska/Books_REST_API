from flask_restful import Resource
import json
from flask import request

from models.book_volume import BookVolume
from resources.saving_finctions_book_volume import save_book_volume
from resources.saving_functions_access_info import save_access_info
from resources.saving_functions_sale_info import save_sale_info
from resources.saving_functions_search_info import save_search_info
from resources.saving_functions_volume_info import save_volume_info


class Db(Resource):
    def post(self):
        data = json.loads(request.data)

        unsaved_internal_id_list = []

        for item in data.get('items'):
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

        return {"message": "Process finished!",
                "warnings": "{}".format(
                    '''Books with the following ids were unsaved, because they already exist in the db: {}'''.format(
                        unsaved_internal_id_list) if unsaved_internal_id_list else None)
                }, 200
