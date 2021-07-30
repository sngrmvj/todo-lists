
import os,sys


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Below is for the setting up of app using the Environmental variable.
app_config = {
    'development': Development, 
    'production': Production,
    'FLASK_ENV': os.getenv('FLASK_ENV'),
    # In the Flask Env we use 'developement or production'. It refers to here which calls the Development and Prouction class
}
