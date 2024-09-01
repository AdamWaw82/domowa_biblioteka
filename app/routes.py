from flask import render_template, flash, redirect, url_for

from app import app, db
from app.forms import AddAuthorForm, AddBookForm
from app.models import Book, Author


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
        flash('Book added successfully!')
        return redirect(url_for('index'))
    return render_template('add_book.html', form=form)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    form = AddAuthorForm()
    if form.validate_on_submit():
        author = Author(name=form.name.data)
        db.session.add(author)
        db.session.commit()
        flash('Author added successfully!')
        return redirect(url_for('index'))
    return render_template('add_author.html', form=form)



@app.route('/get_author', methods=['POST'])
def get_author():
    pass


@app.route('/get_authors_book/<int:author_id>', methods=['GET'])
def get_authors_book(author_id):
    pass


@app.route('/lend_book/<int:book_id>', methods=['POST'])
def lend_book(book_id):
    pass


@app.route('/return_book/<int:book_id>', methods=['POST'])
def return_book(book_id):
    pass
