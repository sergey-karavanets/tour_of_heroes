from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from routes import init as heroes_route

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/tour_of_heroes'
db = SQLAlchemy(app)
ma = Marshmallow(app)

heroes_route(app=app)
