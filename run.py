
from src.initialize_app import create_app
from flask_cors import CORS 
from src.config import app_config



env_name = app_config['FLASK_ENV']
app = create_app(env_name) 
CORS(app) 


if __name__ == "__main__":

    app.run()