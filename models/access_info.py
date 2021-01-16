from db import db


class AccessInfo(db.Model):
    __tablename__ = 'access_info'
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
    viewability_id = db.Column(
        db.Integer(),
        db.ForeignKey('viewability.id')
    )
    embeddable = db.Column(db.Boolean())
    publicDomain = db.Column(db.Boolean())
    textToSpeechPermission_id = db.Column(
        db.Integer(),
        db.ForeignKey('text_to_speech_permission.id')
    )
    epub_id = db.Column(
        db.Integer(),
        db.ForeignKey('epub.id')
    )
    pdf_id = db.Column(
        db.Integer(),
        db.ForeignKey('pdf.id')
    )
    webReaderLink = db.Column(db.String(250))
    accessViewStatus_id= db.Column(
        db.Integer(),
        db.ForeignKey('access_view_status.id')
    )
    quoteSharingAllowed = db.Column(db.Boolean())


class Viewability(db.Model):
    __tablename__ = 'viewability'
    id = db.Column(db.Integer(), primary_key=True)
    viewability_name = db.Column(db.String(50))


class TextToSpeechPermission(db.Model):
    __tablename__ = 'text_to_speech_permission'
    id = db.Column(db.Integer(), primary_key=True)
    permission_type = db.Column(db.String(50))


class EPub(db.Model):
    __tablename__ = 'epub'
    id = db.Column(db.Integer(), primary_key=True)
    isAvailable = db.Column(db.Booelan())


class Pdf(db.Model):
    __tablename__ = 'pdf'
    id = db.Column(db.Integer(), primary_key=True)
    isAvailable = db.Column(db.Booelan())
    acsTokenLink = db.Column(db.String(250))


class AccessViewStatus(db.Model):
    __tablename__ = 'access_view_status'
    id = db.Column(db.Integer(), primary_key=True)
    status = db.Column(db.String(50))