import pytz
from flask import render_template, flash, redirect, url_for

from app import app, db, datetime
from app.forms import AddAuthorForm, AddBookForm, LendBookForm
from app.models import Book, Author, BorrowRecord


@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data)
        ids = Author.id.in_(form.authors.data)
        selected_authors = Author.query.filter(ids).all()
        book.authors.extend(selected_authors)
        db.session.add(book)
        db.session.commit()
        flash('Książka dodana')
        return redirect(url_for('index'))
    return render_template('add_book.html', form=form)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    form = AddAuthorForm()
    if form.validate_on_submit():
        author = Author(name=form.name.data)
        db.session.add(author)
        db.session.commit()
        flash('Autor dodany')
        return redirect(url_for('index'))
    return render_template('add_author.html', form=form)


@app.route('/lend_book/<int:book_id>', methods=['GET', 'POST'])
def lend_book(book_id):
    form = LendBookForm()
    book = Book.query.get_or_404(book_id)
    if form.validate_on_submit():
        record = BorrowRecord(book_id=book_id, borrower=form.borrower.data)
        book.is_on_shelf = False
        db.session.add(record)
        db.session.commit()
        flash('Książka wyporzyczona')
        return redirect(url_for('index'))
    return render_template('lend_book.html', form=form, book=book)


@app.route('/return_book/<int:book_id>', methods=['POST'])
def return_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.is_on_shelf:
        flash('Book is already on the shelf.')
    else:
        record = BorrowRecord.query.filter_by(book_id=book_id, returned_at=None).first()
        record.returned_at = datetime.now(tz=pytz.timezone('Poland'))
        book.is_on_shelf = True
        db.session.commit()
        flash('Książka zwrócona')
    return redirect(url_for('index'))
