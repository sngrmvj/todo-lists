
from src.initialize_app import create_app
from flask_cors import CORS 
from src.config import app_config
from src.model import initialize_db


env_name = app_config['FLASK_ENV']
app = create_app(env_name) 
CORS(app) 


"""Importatnt (IMP)"""
# Create Database and collections if not exists.
# Note - Mongo DB is lazy in creating the DB and collection.
# Note - If you are not creating any record it will not show the created DB and collections. 
# Note - Causes confusion
initialize_db.create_db_collections()



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)