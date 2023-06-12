from flask import Blueprint, jsonify
from flask import request
from common.database import db, project

project_api = Blueprint("project_api", __name__)


@project_api.route("/project_api/creat", methods=['POST'])
def creat_project():
    project_obj = project(project_name='冯俊强', address='1111')
    db.session.add(project_obj)
    db.session.commit()
    return jsonify({
        'code': 20000, 'msg': '创建项目成功', 'success': True
    })


@project_api.route("/project_api/select_list", methods=['POST'])
def select_project():
    project_list = project.query.filter().all()
    # db.session.add(project_list)
    for i in project_list:
        print(i)
    return jsonify({
        'code': 20000, 'msg': '创建项目成功', 'success': True
    })
