from db import db


volume_info_author = db.Table(
    'volume_info_author',
    db.Column(
        'volume_info_id',
        db.Integer(),
        db.ForeignKey('volume_info.id'),
        primary_key=True
    ),
    db.Column(
        'author_id',
        db.Integer(),
        db.ForeignKey('author.id'),
        primary_key=True
    )
)


volume_info_category = db.Table(
    'volume_info_category',
    db.Column(
        'volume_info_id',
        db.Integer(),
        db.ForeignKey('volume_info.id'),
        primary_key=True
    ),
    db.Column(
        'category_id',
        db.Integer(),
        db.ForeignKey('category.id'),
        primary_key=True
    )
)


class VolumeInfo(db.Model):
    __tablename__ = 'volume_info'
    id = db.Column(db.Integer(), primary_key=True)
    book_volume_id = db.Column(
        db.Integer(),
        db.ForeignKey('book_volume.id'),
        nullable=False
    )
    title = db.Column(db.String(300))
    publisher = db.Column(db.String(100))
    publishedDate = db.Column(db.String(50))
    description = db.Column(db.String())
    reading_mode_id = db.Column(
        db.Integer(),
        db.ForeignKey('reading_mode.id')
    )
    printType_id = db.Column(
        db.Integer(),
        db.ForeignKey('print_type.id')
    )
    maturityRating_id = db.Column(
        db.Integer(),
        db.ForeignKey('maturity_rating.id')
    )
    allowAnonLogging = db.Column(db.Boolean())
    contentVersion = db.Column(db.String(50))
    panelizationSummary_id = db.Column(
        db.Integer,
        db.ForeignKey('panelization_summary.id')
    )
    imageLinks_id = db.Column(
        db.Integer,
        db.ForeignKey('image_links.id')
    )
    language_id = db.Column(
        db.Integer(),
        db.ForeignKey('language_code.id')
    )
    previewLink = db.Column(db.String(250))
    infoLink = db.Column(db.String(250))
    canonicalVolumeLink = db.Column(db.String(250))

    authors = db.relationship('Author', secondary=volume_info_author)
    industry_identifiers = db.relationship('IndustryIdentifier')
    categories = db.relationship('Category', secondary=volume_info_category)

    book_volume = db.relationship('BookVolume', back_populates="volume_info")

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class ReadingMode(db.Model):
    __tablename__ = 'reading_mode'
    id = db.Column(db.Integer(), primary_key=True)
    text = (db.Boolean())
    image = (db.Boolean())

    volumes_info = db.relationship('VolumeInfo')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class PrintType(db.Model):
    __tablename__ = 'print_type'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))

    volumes_info = db.relationship('VolumeInfo')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class MaturityRating(db.Model):
    __tablename__ = 'maturity_rating'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))

    volumes_info = db.relationship('VolumeInfo')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class PanelizationSummary(db.Model):
    __tablename__ = 'panelization_summary'
    id = db.Column(db.Integer(), primary_key=True)
    containsEpubBubbles = db.Column(db.Boolean())
    containsImageBubbles = db.Column(db.Boolean())

    volumes_info = db.relationship('VolumeInfo')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class ImageLinks(db.Model):
    __tablename__ = 'image_links'
    id = db.Column(db.Integer(), primary_key=True)
    smallThumbnail = db.Column(db.String(250))
    thumbnail = db.Column(db.String(250))

    volume_info = db.relationship('VolumeInfo')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class LanguageCode(db.Model):
    __tablename__ = 'language_code'
    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String(100))
    language_code = db.Column(db.String(10))

    volumes_info = db.relationship('VolumeInfo')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(150))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class IndustryIdentifier(db.Model):
    __tablename__ = 'industry_identifier'
    id = db.Column(db.Integer(), primary_key=True)
    volume_info_id = db.Column(
        db.Integer(),
        db.ForeignKey('volume_info.id'),
        nullable=False
    )
    type = db.Column(db.String(150))
    identifier = db.Column(db.Integer())

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer(), primary_key=True)
    cat_name = db.Column(db.String(50))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
