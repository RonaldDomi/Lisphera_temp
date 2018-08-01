from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="static/dist", template_folder="static")




from lisphera import routes