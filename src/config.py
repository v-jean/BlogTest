import os

class Development(object):
    #Development environment
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class Production(object):
    #Production environment
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app_config = {
    'development': Development,
    'production': Production,
}

#set DATABASE_URL=postgres://postgres:jplv123.YJ@localhost:5432/blog_api_db
#set JWT_SECRET_KEY = jplv123.YJ
#set FLASK_ENV = development