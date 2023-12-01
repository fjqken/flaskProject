import json
from flask import Blueprint, jsonify
from flask import request
from models.database import db, user_fung

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
        result_error = {"code": 60204, "message": "账号密码错误"}
        return jsonify(result_error)

    # db.session.add(user)
    # db.session.commit()


@app_user.route('/user/loginv2', methods=['post'])
def userl_loginv2():
    login_body = request.json
    user = user_fung.query.filter(user_fung.username == login_body['username']).first()
    if user:
        return jsonify(
            {'code': 200, 'msg': 'success', 'data': {'accessToken': 'admin-accessToken'}})
    else:
        result_error = {"code": 60204, "message": "账号密码错误"}
        return jsonify(result_error)


@app_user.route("/user/info", methods=['GET'])
def info():
    # 获取GET中请求token参数值
    users = {
        'admin-token': {
            'roles': ['admin'],
            'introduction': 'I am a super administrator',
            'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            'name': 'Super Admin'
        },
        'editor-token': {
            'roles': ['editor'],
            'introduction': 'I am an editor',
            'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            'name': 'Normal Editor'
        }
    }
    token = request.args.get('token')
    info = users[token]
    # if token == 'admin-token':
    #     result_success = {
    #         "code": 20000,
    #         "data": {
    #             "roles": ["admin"],
    #             "introduction": "I am a super administrator",
    #             "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
    #             "name": "Super Admin"}
    #     }
    #     return result_success
    # else:
    #     result_error = {"code": 60204, "message": "用户信息获取错误"}
    #     return result_error
    if info:
        return jsonify({"code": 20000, "data": info})
    else:
        result_error = {"code": 60204, "message": "用户信息获取错误"}
        return result_error


@app_user.route("/user/userInfo", methods=['get'])
def userInfo():
    return jsonify({
        'code': 200,
        'msg': 'success',
        'data': {'permissions': ['admin'], 'username': "admin",
                 'avatar|1': [
                     'https://i.gtimg.cn/club/item/face/img/2/15922_100.gif',
                     'https://i.gtimg.cn/club/item/face/img/8/15918_100.gif',
                 ]}
    })


@app_user.route("/user/logout", methods=['post'])
def logout():
    return jsonify({
        'code': 20000,
        'data': 'success'
    })


@app_user.route("/api/getResouceList", methods=['get'])
def getResouceList():
    list1 = [
        {
            'title': 'Nutui',
            'desc': '京东风格的轻量级移动端 Vue 组件库',
            'url': 'https://nutui.jd.com/#/range',
            'logo': 'index/nutui.png',
        },
        {
            'title': 'Vant',
            'desc': '轻量、可靠的移动端 Vue 组件库',
            'url': 'https://vant-contrib.gitee.io/vant/v3/#/zh-CN',
            'logo': 'index/vant.png',
        },
        {
            'title': 'Ant Design',
            'desc': '为 Web 应用提供了丰富的基础 UI 组件',
            'url': 'https://antdv.com/docs/vue/introduce-cn/',
            'logo': 'index/antd.svg',
        },
        {
            'title': 'Vite 中文',
            'desc': '下一代前端开发与构建工具',
            'url': 'https://cn.vitejs.dev/',
            'logo': 'index/vite.svg',
        },
        {
            'title': 'Vue3 文档',
            'desc': '渐进式JavaScript框架vue3中文文档',
            'url': 'https://vue3js.cn/docs/zh/',
            'logo': 'logo.png',
        },
        {
            'title': 'ElementPlus',
            'desc': '一套基于 Vue 3.0 的桌面端组件库',
            'url': 'https://element-plus.gitee.io/#/zh-CN/component/installation',
            'logo': 'index/element+.svg',
        },
        {
            'title': 'Iconpark',
            'desc': '2400+基础图标，29种图标分类，提供更多的选择',
            'url': 'https://iconpark.oceanengine.com/home',
            'logo': 'index/iconpark.svg',
        },
        {
            'title': 'Naiveui',
            'desc': '一个 Vue 3 组件库，使用 TypeScript',
            'url': 'https://www.naiveui.com/zh-CN/light',
            'logo': 'index/naive.svg',
        },
        {
            'title': 'Echarts5.0',
            'desc': '一个基于 JavaScript 的开源可视化图表库',
            'url': 'https://echarts.apache.org/zh/index.html',
            'logo': 'index/echarts.png',
        },
        {
            'title': 'XGplayer',
            'desc': '带解析器、能节省流量的 Web 视频播放器',
            'url': 'http://v2.h5player.bytedance.com/',
            'logo': 'index/xgplayer.png',
        },
        {
            'title': 'VueUse',
            'desc': 'VUE组合实用程序的集合',
            'url': 'https://vueuse.org/',
            'logo': 'index/vueuse.svg',
        },
        {
            'title': 'Vue3 源码',
            'desc': '深入学习了解vue3源码',
            'url': 'https://vue3js.cn/start/',
            'logo': 'logo.png',
        },
    ]
    return jsonify({
        'code': 200,
        'msg': 'success',
        'data': {'list': list1}
    })
