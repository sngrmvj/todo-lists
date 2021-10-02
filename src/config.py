
import os


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



"""App config section"""

# Below is for the setting up of app using the Environmental variable.
app_config = {
    'development': Development, 
    'production': Production,
    'FLASK_ENV': os.getenv('FLASK_ENV'),
    'CORS_URL_ORIGINS' : [
        'http://localhost:4200',
        'http://127.0.0.1:4200',  
    ],
    # In the Flask Env we use 'developement or production'. It refers to here which calls the Development and Prouction class
}

