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


class project(db.Model):
    __table_name__ = "project"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    # 添加项目创建者的外键
    create_user_id = db.Column(db.Integer, db.ForeignKey(user_fung.id))
    create_user = db.relationship("user_fung", backref="project")
