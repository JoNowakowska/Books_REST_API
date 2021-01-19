from sqlalchemy import UniqueConstraint, and_

from db import db


sale_info_offer = db.Table(
    'sale_info_offer',
    db.Column(
        'sale_info_id',
        db.Integer(),
        db.ForeignKey('sale_info.id'),
        primary_key=True
    ),
    db.Column(
        'offer_id',
        db.Integer(),
        db.ForeignKey('offer.id'),
        primary_key=True
    )
)


class SaleInfo(db.Model):
    __tablename__ = 'sale_info'
    id = db.Column(db.Integer(), primary_key=True)
    book_volume_id = db.Column(
        db.Integer(),
        db.ForeignKey('book_volume.id'),
        nullable=False
    )
    country_id = db.Column(
        db.Integer(),
        db.ForeignKey('country_code.id')
    )
    saleability_id = db.Column(
        db.Integer(),
        db.ForeignKey('saleability.id')
    )
    isEbook = db.Column(db.Boolean())
    basic_list_price_id = db.Column(
        db.Integer(),
        db.ForeignKey('basic_list_price.id')
    )
    basic_retail_price_id = db.Column(
        db.Integer(),
        db.ForeignKey('basic_retail_price.id')
    )
    buyLink = db.Column(db.String(250))

    offers = db.relationship('Offer', secondary=sale_info_offer)

    book_volume = db.relationship('BookVolume', back_populates="sale_info")

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class CountryCode(db.Model):
    __tablename__ = 'country_code'
    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String(100))
    country_code = db.Column(db.String(10))

    sales_info = db.relationship('SaleInfo', backref='country_code')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Saleability(db.Model):
    __tablename__ = 'saleability'
    id = db.Column(db.Integer(), primary_key=True)
    option_name = db.Column(db.String(50))

    sales_info = db.relationship('SaleInfo', backref='saleability')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class BasicListPrice(db.Model):
    __tablename__ = 'basic_list_price'
    id = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.Float())
    currencyCode_id = db.Column(
        db.Integer(),
        db.ForeignKey('currency_code.id')
    )

    sales_info = db.relationship('SaleInfo', backref='basic_list_price')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class BasicRetailPrice(db.Model):
    __tablename__ = 'basic_retail_price'
    id = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.Float())
    currencyCode_id = db.Column(
        db.Integer(),
        db.ForeignKey('currency_code.id')
    )

    sales_info = db.relationship('SaleInfo', backref='basic_retail_price')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class CurrencyCode(db.Model):
    __tablename__ = 'currency_code'
    id = db.Column(db.Integer(), primary_key=True)
    currencyCode = db.Column(db.String(10))

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
            return self
        except:
            existing_currency = self.query.filter(CurrencyCode.currencyCode == self.currencyCode).first()
            return existing_currency


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer(), primary_key=True)
    finskyOfferType = db.Column(db.String())
    offer_list_price_id = db.Column(
        db.Integer(),
        db.ForeignKey('offer_list_price.id')
    )
    offer_retail_price_id = db.Column(
        db.Integer(),
        db.ForeignKey('offer_retail_price.id')
    )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self


class OfferListPrice(db.Model):
    __tablename__ = 'offer_list_price'
    id = db.Column(db.Integer(), primary_key=True)
    amountInMicros = db.Column(db.Integer())
    currencyCode_id = db.Column(
        db.Integer(),
        db.ForeignKey('currency_code.id')
    )
    UniqueConstraint(amountInMicros, currencyCode_id)

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
            return self
        except:
            existing_offer_list_price = self.query.filter(
                and_(OfferListPrice.amountInMicros == self.amountInMicros,
                     OfferListPrice.currencyCode_id == self.currencyCode_id).first()
            )
            return existing_offer_list_price


class OfferRetailPrice(db.Model):
    __tablename__ = 'offer_retail_price'
    id = db.Column(db.Integer(), primary_key=True)
    amountInMicros = db.Column(db.Integer())
    currencyCode_id = db.Column(
        db.Integer(),
        db.ForeignKey('currency_code.id')
    )
    UniqueConstraint(amountInMicros, currencyCode_id)

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
            return self
        except:
            existing_offer_retail_price = self.query.filter(
                and_(OfferRetailPrice.amountInMicros == self.amountInMicros,
                     OfferRetailPrice.currencyCode_id == self.currencyCode_id).first()
            )
            return existing_offer_retail_price