from flask_restful import Resource
import json
from flask import request

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
            book_volume_item_id = ''
            try:
                book_volume_item_id = save_book_volume(item)
            except Exception as e:
                print(e)
                unsaved_internal_id_list.append(item.get('id')
                                                if item.get('id')
                                                else 'Unknown ID of a book with an etag {}'.format(item.get('etag'))
                                                )
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
                    '''Books with the following ids were unsaved,
                    most probably because these ids already exist in the db: {}'''.format(
                        unsaved_internal_id_list) if unsaved_internal_id_list else None)
                }, 200


