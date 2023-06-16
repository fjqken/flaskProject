import json

from flask import Blueprint, jsonify
from flask import request
from common.database import db, project, user_fung

project_api = Blueprint("project_api", __name__)


@project_api.route("/project_api/creat", methods=['POST'])
def creat_project():
    data = request.get_data()
    js_data = json.loads(data)
    print(js_data)
    project_obj = project(project_name=js_data['project_name'], address=js_data['address'])
    project_obj.create_user = user_fung.query.filter(user_fung.id == 1).first()
    db.session.add(project_obj)
    db.session.commit()
    return jsonify({
        'code': 20000, 'msg': '创建项目成功', 'success': True
    })


@project_api.route("/project_api/select_list", methods=['POST'])
def select_project():
    user_obj = user_fung.query.filter(user_fung.id == 1).first()
    for project1 in user_obj.project:
        print(project1.project_name)
    # project_list = project.query.filter().all()
    # db.session.add(project_list)
    # for i in project_list:
    #     print(i.project_name)
    return jsonify({
        'code': 20000, 'msg': '查询项目成功', 'success': True
    })
