from app import db
from datetime import datetime as dt

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    date_created = db.Column(db.DateTime(), default=dt.utcnow)