from datetime import datetime

from models.book_volume import BookVolume


def save_book_volume(item):
    book_volume_item = BookVolume(
        kind=item.get('kind'),
        internal_id=item.get('id'),
        etag=item.get('etag'),
        selfLink=item.get('selfLink'),
        created_at=datetime.utcnow()
    )
    book_volume_item.save_to_db()
    book_volume_item_id = book_volume_item.id
    return book_volume_item_id
