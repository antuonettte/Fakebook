from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# setup database connection
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()

from app import routes, models