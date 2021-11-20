import os

class Config:
    # Create the secret key to against protect modify cookie, forturly attack, cross site request
    # Create by -> secrets.token_hex(16)
    SECRET_KEY ='f01cfb0aacd9b3f40902d6027d82ed56'

    # Set the config of the database
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS =True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')