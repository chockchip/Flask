from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms.form import Form

app = Flask(__name__)
# Set a secret key to protect against modifying cookies, cross site foregery attacks
app.config['SECRET_KEY'] = 'fb9ebbfda985875e5d1c1ed15ecddf8a'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

from flask_blog import routes