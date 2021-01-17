from models.search_info import SearchInfo


def save_search_info(item_search_info, book_volume_item_id):
    search_info_item = SearchInfo(
        book_volume_id=book_volume_item_id,
        textSnippet=item_search_info.get('textSnippet')
    )
    search_info_item.save_to_db()