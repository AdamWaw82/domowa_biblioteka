python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


flask db init
flask db migrate -m "Create tables for books, authors"
flask db upgrade


flask run
