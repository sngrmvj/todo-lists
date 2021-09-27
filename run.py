
from src.initialize_app import create_app
from flask_cors import CORS 
from src.config import app_config
from src.model import initialize_db
import os


env_name = app_config['FLASK_ENV']
app = create_app(env_name) 
CORS(app, resources={ r'/*': {'origins': app_config['CORS_URL_ORIGINS']}}, supports_credentials=True)

"""Importatnt (IMP)"""
# Create Database and collections if not exists.
# Note - Mongo DB is lazy in creating the DB and collection.
# Note - If you are not creating any record it will not show the created DB and collections. 
# Note - Causes confusion
initialize_db.create_db_collections()



if __name__ == "__main__":
    app.run(port=os.environ.get('FLASK_PORT'),debug=True)