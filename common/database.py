from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class user_fung(db.Model):
    # 用户表
    __table_name__ = "user_fung"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())


class project(db.Model):
    # 项目表
    __table_name__ = "project"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
    # 添加项目创建者的外键
    create_user_id = db.Column(db.Integer, db.ForeignKey(user_fung.id))
    create_user = db.relationship("user_fung", backref="project")


class api_test(db.Model):
    # 项目表
    __table_name__ = "api_test"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    methods = db.Column(db.String(100))
    headers = db.Column(db.JSON)
    url = db.Column(db.String(100))
    body = db.Column(db.JSON)
    order = db.Column(db.Integer)
    last_time = db.Column(db.DateTime)
    status = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
