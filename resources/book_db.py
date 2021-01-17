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

        for item in data['items']:
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

        return {"message": "Success!!!"}, 200
