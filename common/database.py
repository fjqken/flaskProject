from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class user_fung(db.Model):
    __table_name__ = "user_fung"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
