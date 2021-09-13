
from src.initialize_app import create_app
from flask_cors import CORS 
from src.config import app_config
from src.model import initialize_db


env_name = app_config['FLASK_ENV']
app = create_app(env_name) 
CORS(app) 

# Create Database if not exists
initialize_db.create_database()
# Create collections in the database if not exists
initialize_db.create_collection()


if __name__ == "__main__":
    app.run()