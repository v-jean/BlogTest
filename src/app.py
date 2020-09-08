from flask import Flask
from .config import app_config

def create_app(env_name):
    print(env_name)
    #initialization
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    @app.route('/', methods=['GET'])
    def index():
        #first endpoint
        return "Up and running!"
    
    return app