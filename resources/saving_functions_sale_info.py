from models.sale_info import CountryCode, Saleability, CurrencyCode, BasicListPrice, BasicRetailPrice, SaleInfo, \
    OfferListPrice, OfferRetailPrice, Offer


def save_country_code(item_sale_info):
    country_code_info = item_sale_info.get('country')
    if country_code_info:
        country_code_item = CountryCode(
            country_code=country_code_info
        )
        country_code_item.save_to_db()
        country_code_item_id = country_code_item.id
        return country_code_item_id


def save_saleability(item_sale_info):
    saleability_info = item_sale_info.get('saleability')
    if saleability_info:
        saleability_item = Saleability(
            option_name=saleability_info
        )
        saleability_item.save_to_db()
        saleability_item_id = saleability_item.id
        return saleability_item_id


def save_basic_list_price(item_sale_info):
    basic_list_price_info = item_sale_info.get('listPrice')
    if basic_list_price_info:
        basic_list_price_currency_code_info = basic_list_price_info.get('currencyCode')
        basic_list_price_currency_code_item = CurrencyCode(
            currencyCode=basic_list_price_currency_code_info
        )
        basic_list_price_currency_code_item.save_to_db()
        basic_list_price_currency_code_item_id = basic_list_price_currency_code_item.id
        if basic_list_price_currency_code_item_id:
            basic_list_price_item = BasicListPrice(
                amount=basic_list_price_info.get('amount'),
                currencyCode_id=basic_list_price_currency_code_item_id
            )
            basic_list_price_item.save_to_db()
            basic_list_price_item_id = basic_list_price_item.id
            return basic_list_price_item_id


def save_basic_retail_price(item_sale_info):
    basic_retail_price_info = item_sale_info.get('retailPrice')
    if basic_retail_price_info:
        basic_retail_price_currency_code_info = basic_retail_price_info.get('currencyCode')
        basic_retail_price_currency_code_item = CurrencyCode(
            currencyCode=basic_retail_price_currency_code_info
        )
        basic_retail_price_currency_code_item.save_to_db()
        basic_retail_price_currency_code_item_id = basic_retail_price_currency_code_item.id
        if basic_retail_price_currency_code_item_id:
            basic_retail_price_item = BasicRetailPrice(
                amount=basic_retail_price_info.get('amount'),
                currencyCode_id=basic_retail_price_currency_code_item_id
            )
            basic_retail_price_item.save_to_db()
            basic_retail_price_item_id = basic_retail_price_item.id
            return basic_retail_price_item_id


def save_offers(item_sale_info):
    offers_list = item_sale_info.get('offers')
    if offers_list:
        saved_offers_list = []
        for o in offers_list:
            offer_finsky_offer_type = o.get('finskyOfferType')
            list_price_info = o.get('listPrice')
            retail_price_info = o.get('retailPrice')
            if list_price_info:
                list_price_amount_in_micros = list_price_info.get('amountInMicros')
                list_price_currency_code = list_price_info.get('currencyCode')
                currency_code_item = CurrencyCode(
                    currencyCode=list_price_currency_code
                )
                currency_code_object = currency_code_item.save_to_db()
                currency_code_id = currency_code_object.id
                offer_list_price_item = OfferListPrice(
                    amountInMicros=list_price_amount_in_micros,
                    currencyCode_id=currency_code_id
                )
                offer_list_price_object = offer_list_price_item.save_to_db()
                offer_list_price_id = offer_list_price_object.id
            if retail_price_info:
                retail_price_amount_in_micros = list_price_info.get('amountInMicros')
                retail_price_currency_code = list_price_info.get('currencyCode')
                currency_code_item = CurrencyCode(
                    currencyCode=retail_price_currency_code
                )
                currency_code_object = currency_code_item.save_to_db()
                currency_code_id = currency_code_object.id
                offer_retail_price_item = OfferRetailPrice(
                    amountInMicros=retail_price_amount_in_micros,
                    currencyCode_id=currency_code_id
                )
                offer_retail_price_object = offer_retail_price_item.save_to_db()
                offer_retail_price_id = offer_retail_price_object.id
            offer_item = Offer(
                finskyOfferType=offer_finsky_offer_type,
                offer_list_price_id=offer_list_price_id,
                offer_retail_price_id=offer_retail_price_id
            )
            new_saved_offer = offer_item.save_to_db()
            saved_offers_list.append(new_saved_offer)
        return saved_offers_list


def save_sale_info(item_sale_info, book_volume_item_id):
    country_code_item_id = save_country_code(item_sale_info)
    saleability_item_id = save_saleability(item_sale_info)
    basic_list_price_item_id = save_basic_list_price(item_sale_info)
    basic_retail_price_item_id = save_basic_retail_price(item_sale_info)
    #saved_offers_list = save_offers(item_sale_info)
    sale_info_item = SaleInfo(
        book_volume_id=book_volume_item_id,
        country_id=country_code_item_id,
        saleability_id=saleability_item_id,
        isEbook=item_sale_info.get('isEbook'),
        basic_list_price_id=basic_list_price_item_id,
        basic_retail_price_id=basic_retail_price_item_id,
        buyLink=item_sale_info.get('buyLink'),
        #offers=saved_offers_list
    )
    sale_info_item.save_to_db()
