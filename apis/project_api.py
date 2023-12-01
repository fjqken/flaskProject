import json

from flask import Blueprint, jsonify
from flask import request

from models.database import db, project, user_fung

project_api = Blueprint("project_api", __name__)


@project_api.route("/project_api/creat_project", methods=['POST'])
def creat_project():
    data = request.get_data()
    js_data = json.loads(data)
    print(js_data)
    project_obj = project(project_name=js_data['project_name'], address=js_data['address'])
    project_obj.create_user = user_fung.query.filter(user_fung.id == 1).first()
    db.session.add(project_obj)
    db.session.flush()
    db.session.commit()
    return jsonify({
        'code': 20000, 'msg': '创建项目成功', 'success': True
    })


@project_api.route("/project_api/select_list", methods=['POST'])
def select_project():
    request_body = request.get_json()
    return_project_list = []
    if request_body == {}:
        project_list = project.query.filter().all()
    else:
        filters = (project.create_user_id == request_body['create_user_id'],
                   project.project_name.like("%" + request_body['project_name'] + "%"))
        project_list = project.query.filter(*filters).all()
    for project_obj in project_list:
        return_project_list.append({"id": project_obj.id, 'project_name': project_obj.project_name,
                                    'create_time': project_obj.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                                    'address': project_obj.address})
    return jsonify({
        "code": 20000, "msg": "查询项目成功", "success": True, "data": return_project_list
    })
