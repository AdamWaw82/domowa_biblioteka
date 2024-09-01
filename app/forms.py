from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired
from app.models import Author


class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    authors = SelectMultipleField('Authors', coerce=int)
    submit = SubmitField('Add Book')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.authors.choices = [(author.id, author.name) for author in Author.query.all()]


class AddAuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add Author')


class LendBookForm(FlaskForm):
    borrower = StringField('Borrower Name', validators=[DataRequired()])
    submit = SubmitField('Lend Book')


class ReturnBookForm(FlaskForm):
    submit = SubmitField('Return Book')
