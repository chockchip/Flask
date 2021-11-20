from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

# Create instance of the database
# Command to create dabase -> db.create_all()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

# login is function name of ours route
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


mail = Mail()

# Register route from the blue print


def create_app(config_class=Config):
    # Create instance opf Flask class
    # __name__ -> Special variable that show the name of the Module
    # __name__ -> It will return "main" if we call it on the Module itself
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import erros
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(erros)

    return app
