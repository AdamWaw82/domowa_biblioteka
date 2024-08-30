from flask import render_template

from app import app
from app.models import Book


@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/add_book', methods=['POST'])
def add_book():
    pass


@app.route('/get_book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    pass


@app.route('/add_author', methods=['POST'])
def add_author():
    pass


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
