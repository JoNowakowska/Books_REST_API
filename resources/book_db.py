from flask_restful import Resource, reqparse
import json
from flask import request
from datetime import datetime

from models.access_info import AccessInfo, Viewability, TextToSpeechPermission, EPub, Pdf, AccessViewStatus
from models.book_volume import BookVolume
from models.sale_info import SaleInfo, CountryCode, Saleability, BasicListPrice, CurrencyCode, BasicRetailPrice
from models.search_info import SearchInfo
from models.volume_info import VolumeInfo, IndustryIdentifier, PrintType, MaturityRating, PanelizationSummary, \
    ImageLinks, LanguageCode, ReadingMode


class Db(Resource):
    def post(self):
        #data_parser = reqparse.RequestParser()
        #data_parser.add_argument("items",
        #                         required=True,
         #                        type=str,
         #                        help="Please add items.")
        #data = data_parser.parse_args()

        data = json.loads(request.data)

        for item in data['items']:
            book_volume_item = BookVolume(
                kind=item['kind'],
                internal_id=item['id'],
                etag=item['etag'],
                selfLink=item['selfLink'],
                created_at=datetime.utcnow()
            )
            book_volume_item.save_to_db()
            book_volume_item_id = book_volume_item.id

            item_volume_info = item['volumeInfo']

            reading_mode_info = item_volume_info['readingModes']
            reading_mode_item = ReadingMode(
                text=reading_mode_info['text'],
                image=reading_mode_info['image']
            )
            reading_mode_item.save_to_db()
            reading_mode_item_id = reading_mode_item.id

            print_type_info = item_volume_info['printType']
            print_type_item = PrintType(
                name=print_type_info
            )
            print_type_item.save_to_db()
            print_type_item_id = print_type_item.id

            maturity_rating_info = item_volume_info['maturityRating']
            maturity_rating_item = MaturityRating(
                name=maturity_rating_info
            )
            maturity_rating_item.save_to_db()
            maturity_rating_item_id = maturity_rating_item.id

            panelization_summary_info = item_volume_info['panelizationSummary']
            panelization_summary_item = PanelizationSummary(
                containsEpubBubbles=panelization_summary_info['containsEpubBubbles'],
                containsImageBubbles=panelization_summary_info['containsImageBubbles']
            )
            panelization_summary_item.save_to_db()
            panelization_summary_item_id = panelization_summary_item.id

            image_links_info = item_volume_info['imageLinks']
            image_links_item = ImageLinks(
                smallThumbnail=image_links_info['smallThumbnail'],
                thumbnail=image_links_info['thumbnail']
            )
            image_links_item.save_to_db()
            image_links_item_id = image_links_item.id

            language_code_info = item_volume_info['language']
            language_code_item = LanguageCode(
                language_code=language_code_info
            )
            language_code_item.save_to_db()
            language_code_item_id = language_code_item.id

            # DODAC AUTORA I KILKA INNYCH BRAKOW!!!!

            volume_info_item = VolumeInfo(
                book_volume_id=book_volume_item_id,
                title=item_volume_info['title'],
                publisher=item_volume_info['publisher'],
                publishedDate=item_volume_info['publishedDate'],
                description=item_volume_info['description'],
                reading_mode_id=reading_mode_item_id,
                printType_id=print_type_item_id,
                maturityRating_id=maturity_rating_item_id,
                allowAnonLogging=item_volume_info['allowAnonLogging'],
                contentVersion=item_volume_info['contentVersion'],
                panelizationSummary_id=panelization_summary_item_id,
                imageLinks_id=image_links_item_id,
                language_id=language_code_item_id,
                previewLink=item_volume_info['previewLink'],
                infoLink=item_volume_info['infoLink'],
                canonicalVolumeLink=item_volume_info['canonicalVolumeLink']
            )
            volume_info_item.save_to_db()
            volume_info_item_id = volume_info_item.id

            industry_identifier_info = item_volume_info['industryIdentifiers']
            for identifier in industry_identifier_info:
                industry_identifier_item = IndustryIdentifier(
                    volume_info_id=volume_info_item_id,
                    type=identifier['type'],
                    identifier=identifier['identifier']
                )
                industry_identifier_item.save_to_db()

            item_sale_info = item['saleInfo']

            country_code_info = item_sale_info['country']

            country_code_item = CountryCode(
                country_code=country_code_info
            )
            country_code_item.save_to_db()
            country_code_item_id = country_code_item.id

            saleability_info = item_sale_info['saleability']

            saleability_item = Saleability(
                option_name=saleability_info
            )
            saleability_item.save_to_db()
            saleability_item_id = saleability_item.id

            basic_list_price_info = item_sale_info['listPrice']
            basic_list_price_currency_code_info = basic_list_price_info['currencyCode']
            basic_list_price_currency_code_item = CurrencyCode(
                currencyCode=basic_list_price_currency_code_info
            )
            basic_list_price_currency_code_item.save_to_db()
            basic_list_price_currency_code_item_id = basic_list_price_currency_code_item.id

            basic_list_price_item = BasicListPrice(
                amount=basic_list_price_info['amount'],
                currencyCode_id=basic_list_price_currency_code_item_id
            )
            basic_list_price_item.save_to_db()
            basic_list_price_item_id = basic_list_price_item.id

            basic_retail_price_info = item_sale_info['retailPrice']
            basic_retail_price_currency_code_info = basic_retail_price_info['currencyCode']
            basic_retail_price_currency_code_item = CurrencyCode(
                currencyCode=basic_retail_price_currency_code_info
            )
            basic_retail_price_currency_code_item.save_to_db()
            basic_retail_price_currency_code_item_id = basic_retail_price_currency_code_item.id

            basic_retail_price_item = BasicRetailPrice(
                amount=basic_retail_price_info['amount'],
                currencyCode_id=basic_retail_price_currency_code_item_id
            )
            basic_retail_price_item.save_to_db()
            basic_retail_price_item_id = basic_retail_price_item.id

            sale_info_item = SaleInfo(
                book_volume_id=book_volume_item_id,
                country_id=country_code_item_id,
                saleability_id=saleability_item_id,
                isEbook=item_sale_info['isEbook'],
                basic_list_price_id=basic_list_price_item_id,
                basic_retail_price_id=basic_retail_price_item_id,
                buyLink=item_sale_info['buyLink']
            )
            sale_info_item.save_to_db()

            # TRZEBA BEDZIE TEZ TU DODAC (OFFERS I MOZE COS JESZCZE)

            item_access_info = item['accessInfo']

            country_code_info = item_access_info['country']

            country_code_item = CountryCode(
                country_code=country_code_info
            )
            country_code_item.save_to_db()
            country_code_item_id = country_code_item.id

            viewability_info = item_access_info['viewability']
            viewability_item = Viewability(
                viewability_name=viewability_info
            )
            viewability_item.save_to_db()
            viewability_item_id = viewability_item.id

            text_to_speech_permission_info = item_access_info['textToSpeechPermission']
            text_to_speech_permission_item = TextToSpeechPermission(
                permission_type=text_to_speech_permission_info
            )
            text_to_speech_permission_item.save_to_db()
            text_to_speech_permission_item_id = text_to_speech_permission_item.id

            epub_info = item_access_info['epub']
            epub_item = EPub(
                isAvailable=epub_info['isAvailable']
            )
            epub_item.save_to_db()
            epub_item_id = epub_item.id

            pdf_info = item_access_info['pdf']
            pdf_item = Pdf(
                isAvailable=pdf_info['isAvailable'],
                acsTokenLink=pdf_info['acsTokenLink']
            )
            pdf_item.save_to_db()
            pdf_item_id = pdf_item.id

            access_view_status_info = item_access_info['accessViewStatus']
            access_view_status_item = AccessViewStatus(
                status=access_view_status_info
            )
            access_view_status_item.save_to_db()
            access_view_status_item_id = access_view_status_item.id

            access_info_item = AccessInfo(
                book_volume_id=book_volume_item_id,
                country_id=country_code_item_id,
                viewability_id=viewability_item_id,
                embeddable=item_access_info['embeddable'],
                publicDomain=item_access_info['publicDomain'],
                textToSpeechPermission_id=text_to_speech_permission_item_id,
                epub_id=epub_item_id,
                pdf_id=pdf_item_id,
                webReaderLink=item_access_info['webReaderLink'],
                accessViewStatus_id=access_view_status_item_id,
                quoteSharingAllowed=item_access_info['quoteSharingAllowed']
            )
            access_info_item.save_to_db()

            item_search_info = item['searchInfo']
            search_info_item = SearchInfo(
                book_volume_id=book_volume_item_id,
                textSnippet=item_search_info['textSnippet']
            )
            search_info_item.save_to_db()

            return {"message": "Success!!!"}, 200
