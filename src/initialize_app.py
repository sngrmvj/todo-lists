
from flask import Flask
from src.config import app_config 
from models.initialize_db import db


def create_app(env_name):
  """
  Create app
  """

  
  # app initiliazation
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])
  db.init_app(app) 


  # Add Blueprints here 


  return app