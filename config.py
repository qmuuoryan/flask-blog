import os

class Config:
    """
    This is the class which will contain the general configurations
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = "app/static/photos"

class DevConfig(Config):
  
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:1234@localhost/blog'
    DEBUG = True

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:1234@localhost/blog_test'

config_options = {
    "development": DevConfig,
    "test": TestConfig,
    "production": ProdConfig
}


