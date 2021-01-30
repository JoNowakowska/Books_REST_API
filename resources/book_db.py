from flask_restful import Resource, reqparse

from .saving_functions_main import get_items_from_url, save_items


class Db(Resource):
    def post(self):

        data_parser = reqparse.RequestParser()
        data_parser.add_argument('q',
                                 required=True,
                                 type=str,
                                 help='Please add keyword(s) you want to search for.')

        data = data_parser.parse_args()
        q = data['q']
        items_to_save_to_db = get_items_from_url(q)

        unsaved_internal_id_list = save_items(items_to_save_to_db)

        return {"message": "Process finished!",
                "warnings": "{}".format(
                    '''Books with the following ids were unsaved, because they already exist in the db: {}'''.format(
                        unsaved_internal_id_list) if unsaved_internal_id_list else None)
                }, 200


