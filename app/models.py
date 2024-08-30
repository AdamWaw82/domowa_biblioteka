from app import db, datetime


books_authors = db.Table('books_authors', db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                         db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
                         )


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    authors = db.relationship('Author', secondary=books_authors, backref=db.backref('books', lazy='dynamic'))
    is_on_shelf = db.Column(db.Boolean, default=True)
    borrow_records = db.relationship('BorrowRecord', backref='book', lazy=True)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)


class BorrowRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrower = db.Column(db.String(120), nullable=False)
    borrowed_at = db.Column(db.DateTime, default=datetime.utcnow)
    returned_at = db.Column(db.DateTime, nullable=True)
