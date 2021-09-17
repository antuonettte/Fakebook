from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash
from app.blueprints.main import db, login_manager

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    date_created = db.Column(db.DateTime(), default=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

