import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///home_library.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '#42lknbxcf8342'
