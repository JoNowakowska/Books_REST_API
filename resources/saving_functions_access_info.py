from models.access_info import Viewability, TextToSpeechPermission, EPub, Pdf, AccessViewStatus, AccessInfo
from models.sale_info import CountryCode


def save_country_code(item_access_info):
    country_code_info = item_access_info.get('country')
    if country_code_info:
        country_code_item = CountryCode(
            country_code=country_code_info
        )
        country_code_item.save_to_db()
        country_code_item_id = country_code_item.id
        return country_code_item_id


def save_viewability(item_access_info):
    viewability_info = item_access_info.get('viewability')
    if viewability_info:
        viewability_item = Viewability(
            viewability_name=viewability_info
        )
        viewability_item.save_to_db()
        viewability_item_id = viewability_item.id
        return viewability_item_id


def save_text_to_speech_permission(item_access_info):
    text_to_speech_permission_info = item_access_info.get('textToSpeechPermission')
    if text_to_speech_permission_info:
        text_to_speech_permission_item = TextToSpeechPermission(
            permission_type=text_to_speech_permission_info
        )
        text_to_speech_permission_item.save_to_db()
        text_to_speech_permission_item_id = text_to_speech_permission_item.id
        return text_to_speech_permission_item_id


def save_epub(item_access_info):
    epub_info = item_access_info.get('epub')
    if epub_info:
        epub_item = EPub(
            isAvailable=epub_info.get('isAvailable')
        )
        epub_item.save_to_db()
        epub_item_id = epub_item.id
        return epub_item_id


def save_pdf(item_access_info):
    pdf_info = item_access_info.get('pdf')
    if pdf_info:
        pdf_item = Pdf(
            isAvailable=pdf_info.get('isAvailable'),
            acsTokenLink=pdf_info.get('acsTokenLink')
        )
        pdf_item.save_to_db()
        pdf_item_id = pdf_item.id
        return pdf_item_id


def save_access_view_status(item_access_info):
    access_view_status_info = item_access_info.get('accessViewStatus')
    if access_view_status_info:
        access_view_status_item = AccessViewStatus(
            status=access_view_status_info
        )
        access_view_status_item.save_to_db()
        access_view_status_item_id = access_view_status_item.id
        return access_view_status_item_id


def save_access_info(item_access_info, book_volume_item_id):
    country_code_item_id = save_country_code(item_access_info)
    viewability_item_id = save_viewability(item_access_info)
    text_to_speech_permission_item_id = save_text_to_speech_permission(item_access_info)
    epub_item_id = save_epub(item_access_info)
    pdf_item_id = save_pdf(item_access_info)
    access_view_status_item_id = save_access_view_status(item_access_info)

    access_info_item = AccessInfo(
        book_volume_id=book_volume_item_id,
        country_id=country_code_item_id,
        viewability_id=viewability_item_id,
        embeddable=item_access_info.get('embeddable'),
        publicDomain=item_access_info.get('publicDomain'),
        textToSpeechPermission_id=text_to_speech_permission_item_id,
        epub_id=epub_item_id,
        pdf_id=pdf_item_id,
        webReaderLink=item_access_info.get('webReaderLink'),
        accessViewStatus_id=access_view_status_item_id,
        quoteSharingAllowed=item_access_info.get('quoteSharingAllowed')
    )
    access_info_item.save_to_db()