import json
from flask import Blueprint, jsonify
from flask import request
from common.database import db, user_fung

app_user = Blueprint("app_user", __name__)


@app_user.route('/login')
def login():
    data = request.get_data()
    js_data = json.loads(data)
    return js_data


@app_user.route('/user/<int:user_id>')
def user_detail(user_id):
    return "您的ID是 %s" % user_id


# 查询字符串形式传参
@app_user.route('/user/user_list')
def user_list():
    # argument:参数
    # request.args:不可变类字典类型
    value = request.args
    # 转为可变字典
    value1 = value.to_dict()
    print(value1['page'])
    page = request.args.get("page", default=1, type=int)
    return "您的page是{page:.2f}".format(page=page)


@app_user.route('/db_test')
def db_test1():
    with db.engine.connect() as conn:
        rs = conn.execute("select 1")
        print(rs.fetchone())
    return str(rs.fetchone())


@app_user.route('/user/create', methods=['POST', 'GET'])
def create_user():
    user = user_fung(username='冯俊强', password='1111')
    db.session.add(user)
    db.session.commit()
    return '成功'


@app_user.route('/user/get_user', methods=['get'])
def get_user():
    comment = request.args.get("content")
    # user = user_fung.query.get(1)
    print(comment)
    users = user_fung.query.filter(user_fung.username == "冯俊强").all()
    print(dict(users))
    for i in users:
        print(i.username)
    gender = request.args.get('gender')
    name = request.args.get('name')
    return jsonify({'name': name, 'gender': gender})


@app_user.route('/user/update_user', methods=['post'])
def update_user():
    user_id = request.json['user_id']
    user = user_fung.query.filter(user_fung.id == user_id).first()
    user.password = request.json['password']
    print(request.remote_addr)
    db.session.commit()
    return jsonify({'name': user.username, 'password': user.password})


@app_user.route('/user/delete_user', methods=['delete'])
def delete_user():
    user_id = request.json['user_id']
    user = user_fung.query.filter(user_fung.id == user_id).first()
    db.session.delete(user)
    db.session.commit()
    return "删除%s成功了" % user_id


@app_user.route('/user/login', methods=['post'])
def userl_login():
    login_body = request.json
    user = user_fung.query.filter(user_fung.username == login_body['username']).first()
    if user:
        return jsonify(
            {'code': 20000, 'msg': '登录成功', 'data': {'user_id': user.id, 'token': "admin-token"}, 'success': True})
    else:
        return jsonify({'success': False, 'msg': '登录失败'})

    # db.session.add(user)
    # db.session.commit()
