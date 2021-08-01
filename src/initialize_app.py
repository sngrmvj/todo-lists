
from flask import Flask
from flask_pymongo import PyMongo
import os,sys
sys.path.append(os.path.abspath('./src/')) 
from src.config import app_config 
from src.views.general import general_api


def create_app(env_name):
  """
    Note - Create app
  """

  # app initiliazation
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])
  mongodb_client = PyMongo(app, uri=os.getenv("DATABASE_URL"))
  app.config['db_connect'] = mongodb_client.db


  # Add Blueprints here 
  app.register_blueprint(general_api, url_prefix='todo/v1/general') 


  return app