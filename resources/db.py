from flask_restful import Resource, reqparse
from datetime import datetime

from models.book_volume import BookVolume
from models.volume_info import VolumeInfo, IndustryIdentifier, PrintType, MaturityRating, PanelizationSummary, \
    ImageLinks, LanguageCode


class Db(Resource):
    def post(self):
        data_parser = reqparse.RequestParser()
        data = data_parser.parse_args()

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

        '''
        DOKONCZYC ZAPISYWANIE w powyzszej metodzie - kontynuuj od saleInfo - po kolei to co jest nizej
            {
                "volumeInfo": {
                    ..........
                    

                "saleInfo": {
                    "country": "PL",
                    "saleability": "FOR_SALE",
                    "isEbook": true,
                    "listPrice": {
                        "amount": 9.58,
                        "currencyCode": "PLN"
                    },
                    "retailPrice": {
                        "amount": 9.58,
                        "currencyCode": "PLN"
                    },
                    "buyLink": "https://play.google.com/store/books/details?id=biIREAAAQBAJ&rdid=book-biIREAAAQBAJ&rdot=1&source=gbs_api",
                    "offers": [
                        {
                            "finskyOfferType": 1,
                            "listPrice": {
                                "amountInMicros": 9580000,
                                "currencyCode": "PLN"
                            },
                            "retailPrice": {
                                "amountInMicros": 9580000,
                                "currencyCode": "PLN"
                            }
                        }
                    ]
                },
                "accessInfo": {
                    "country": "PL",
                    "viewability": "PARTIAL",
                    "embeddable": true,
                    "publicDomain": false,
                    "textToSpeechPermission": "ALLOWED",
                    "epub": {
                        "isAvailable": false
                    },
                    "pdf": {
                        "isAvailable": true,
                        "acsTokenLink": "http://books.google.pl/books/download/LEGO_The_Hobbit-sample-pdf.acsm?id=biIREAAAQBAJ&format=pdf&output=acs4_fulfillment_token&dl_type=sample&source=gbs_api"
                    },
                    "webReaderLink": "http://play.google.com/books/reader?id=biIREAAAQBAJ&hl=&printsec=frontcover&source=gbs_api",
                    "accessViewStatus": "SAMPLE",
                    "quoteSharingAllowed": false
                },
                "searchInfo": {
                    "textSnippet": "LEGO The \u003cb\u003eHobbit\u003c/b\u003e w 10 prostych krokach jest poradnikiem do gry LEGO The \u003cbr\u003e\n\u003cb\u003eHobbit\u003c/b\u003e adresowanym w głównej mierze do osób rozpoczynających swoją \u003cbr\u003e\nprzygodę z wirtualnym Śródziemiem zbudowanym ze słynnych duńskich klocków\u003cbr\u003e\n. Niniejszy&nbsp;..."
                }
            }'''
