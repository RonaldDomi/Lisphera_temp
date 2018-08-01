# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    # temporary route
    @app.route('/')
    def hello_world():

        db = MySQLdb.connect("localhost", "lf_admin", "lisphera2018","lisphera_db")
        cur = db.cursor()
        query = "select * from test;"
        
        cur.execute(query)
        data = cur.fetchall()

        return data.json_encoder()




    return app
