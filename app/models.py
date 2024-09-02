from app import db, datetime
import pytz


class BookAuthor(db.Model):
    __tablename__ = 'book_author'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    is_on_shelf = db.Column(db.Boolean, default=True)
    authors = db.relationship('Author', secondary='book_author', backref=db.backref('books', lazy=True))
    borrow_records = db.relationship('BorrowRecord', backref='book', lazy=True)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)


class BorrowRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrower = db.Column(db.String(120), nullable=False)
    borrowed_at = db.Column(db.DateTime, default=datetime.now(tz=pytz.timezone('Poland')))
    returned_at = db.Column(db.DateTime, nullable=True)
