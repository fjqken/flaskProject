from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class user_fung(db.Model):
    __table_name__ = "user_fung"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


