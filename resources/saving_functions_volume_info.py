from models.volume_info import PrintType, MaturityRating, PanelizationSummary, \
    ImageLinks, LanguageCode, ReadingMode, IndustryIdentifier, VolumeInfo, Author, Category


def save_authors(item_volume_info):
    authors_list = item_volume_info.get('authors')
    if authors_list:
        saved_authors_list = []
        for a in authors_list:
            author_item = Author(
                name=a
            )
            author = author_item.save_to_db()
            saved_authors_list.append(author)
        return saved_authors_list


def save_temp_authors(item_volume_info):
    authors_list = item_volume_info.get('authors')
    if authors_list:
        authors_str = ', '.join([str(author) for author in authors_list])
        return authors_str


def save_reading_mode(item_volume_info):
    reading_mode_info = item_volume_info.get('readingModes')
    if reading_mode_info:
        reading_mode_item = ReadingMode(
            text=reading_mode_info.get('text'),
            image=reading_mode_info.get('image')
        )
        reading_mode_item.save_to_db()
        reading_mode_item_id = reading_mode_item.id
        return reading_mode_item_id


def save_print_type(item_volume_info):
    print_type_info = item_volume_info.get('printType')
    if print_type_info:
        print_type_item = PrintType(
            name=print_type_info
        )
        print_type_item.save_to_db()
        print_type_item_id = print_type_item.id
        return print_type_item_id


def save_categories(item_volume_info):
    categories_list = item_volume_info.get('categories')
    if categories_list:
        saved_categories_list = []
        for c in categories_list:
            category_item = Category(
                cat_name=c
            )
            category = category_item.save_to_db()
            saved_categories_list.append(category)
        return saved_categories_list


def save_temp_categories(item_volume_info):
    categories_list = item_volume_info.get('categories')
    if categories_list:
        categories_str = ', '.join([str(category) for category in categories_list])
        return categories_str


def save_maturity_rating(item_volume_info):
    maturity_rating_info = item_volume_info.get('maturityRating')
    if maturity_rating_info:
        maturity_rating_item = MaturityRating(
            name=maturity_rating_info
        )
        maturity_rating_item.save_to_db()
        maturity_rating_item_id = maturity_rating_item.id
        return maturity_rating_item_id


def save_panelization_summary(item_volume_info):
    panelization_summary_info = item_volume_info.get('panelizationSummary')
    if panelization_summary_info:
        panelization_summary_item = PanelizationSummary(
            containsEpubBubbles=panelization_summary_info.get('containsEpubBubbles'),
            containsImageBubbles=panelization_summary_info.get('containsImageBubbles')
        )
        panelization_summary_item.save_to_db()
        panelization_summary_item_id = panelization_summary_item.id
        return panelization_summary_item_id


def save_image_links(item_volume_info):
    image_links_info = item_volume_info.get('imageLinks')
    if image_links_info:
        image_links_item = ImageLinks(
            smallThumbnail=image_links_info.get('smallThumbnail'),
            thumbnail=image_links_info.get('thumbnail')
        )
        image_links_item.save_to_db()
        image_links_item_id = image_links_item.id
        return image_links_item_id


def save_language_code(item_volume_info):
    language_code_info = item_volume_info.get('language')
    if language_code_info:
        language_code_item = LanguageCode(
            language_code=language_code_info
        )
        language_code_item.save_to_db()
        language_code_item_id = language_code_item.id
        return language_code_item_id


def save_industry_identifier(item_volume_info, volume_info_item_id):
    industry_identifier_info = item_volume_info.get('industryIdentifiers')
    if industry_identifier_info:
        for identifier in industry_identifier_info:
            industry_identifier_item = IndustryIdentifier(
                volume_info_id=volume_info_item_id,
                type=identifier.get('type'),
                identifier=identifier.get('identifier')
            )
            industry_identifier_item.save_to_db()


def save_volume_info(item_volume_info, book_volume_item_id):
    reading_mode_item_id = save_reading_mode(item_volume_info)
    print_type_item_id = save_print_type(item_volume_info)
    maturity_rating_item_id = save_maturity_rating(item_volume_info)
    panelization_summary_item_id = save_panelization_summary(item_volume_info)
    image_links_item_id = save_image_links(item_volume_info)
    language_code_item_id = save_language_code(item_volume_info)
    #saved_authors_list = save_authors(item_volume_info)
    temp_authors_str = save_temp_authors(item_volume_info)
    #saved_categories_list = save_categories(item_volume_info)
    temp_categories_str = save_temp_categories(item_volume_info)

    volume_info_item = VolumeInfo(
        book_volume_id=book_volume_item_id,
        authors=temp_authors_str,
        title=item_volume_info.get('title'),
        publisher=item_volume_info.get('publisher'),
        publishedDate=item_volume_info.get('publishedDate'),
        description=item_volume_info.get('description'),
        reading_mode_id=reading_mode_item_id,
        printType_id=print_type_item_id,
        categories=temp_categories_str,
        averageRating=item_volume_info.get('averageRating'),
        ratingsCount=item_volume_info.get('ratingsCount'),
        maturityRating_id=maturity_rating_item_id,
        allowAnonLogging=item_volume_info.get('allowAnonLogging'),
        contentVersion=item_volume_info.get('contentVersion'),
        panelizationSummary_id=panelization_summary_item_id,
        imageLinks_id=image_links_item_id,
        language_id=language_code_item_id,
        previewLink=item_volume_info.get('previewLink'),
        infoLink=item_volume_info.get('infoLink'),
        canonicalVolumeLink=item_volume_info.get('canonicalVolumeLink')
    )
    volume_info_item.save_to_db()
    volume_info_item_id = volume_info_item.id
    save_industry_identifier(item_volume_info, volume_info_item_id)