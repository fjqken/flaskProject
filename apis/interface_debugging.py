import json

from flask import Blueprint, jsonify
from flask import request
import requests as interface_request
from sqlalchemy import or_, and_
from models.database import db, user_fung, api_test
from flask import current_app
# from flask_sqlalchemy import Pagination

interface_debugging = Blueprint("interface_debugging", __name__)


@interface_debugging.route("/interface_debugging/interface_test", methods=['POST'])
def interface_test():
    request_body = request.json
    methods = request_body['methods']
    headers = request_body['headers']
    url = request_body['url']
    body = request_body['body']
    if methods == "post":
        res = interface_request.post(headers=headers, url=url, json=body)
        return {'code': int(res.status_code), 'elapsed': str(res.elapsed)}
    if methods == "get":
        res = interface_request.get(url=url)
        return jsonify(
            {'code': 20000, 'msg': '请求成功',
             'data': {'code': int(res.status_code), 'elapsed': str(res.elapsed)},
             'success': True})


@interface_debugging.route("/interface_debugging/crate_interface_test", methods=['POST'])
def crate_interface_test():
    try:
        request_body = request.json
        name = request_body['name']
        methods = request_body['methods']
        headers = request_body['headers']
        url = request_body['url']
        body = request_body['body']
        order = request_body['order']
        status = request_body['status']
        interface_test_obj = api_test(name=name, methods=methods, headers=headers, url=url, body=body, order=order,
                                      status=status)
        db.session.add(interface_test_obj)
        db.session.commit()
        # user = api_test.query.filter().all()
        return jsonify(
            {'code': 20000, 'msg': '请求成功',
             'success': True})
    except Exception as e:
        print(e)
        return {'success': False, 'msg': e}
    finally:
        db.session.close()


@interface_debugging.route("/interface_debugging/updata_interface_test", methods=['POST'])
def updata_interface_test():
    try:
        request_body = request.json
        interface_test_id = request_body['id']
        obj = api_test.query.filter(api_test.id == interface_test_id).first()
        obj.name = request_body['name']
        obj.methods = request_body['methods']
        obj.headers = request_body['headers']
        obj.url = request_body['url']
        obj.body = request_body['body']
        obj.order = request_body['order']
        obj.status = request_body['status']
        db.session.commit()
        # user = api_test.query.filter().all()
        return jsonify(
            {'code': 200, 'msg': '请求成功',
             'success': True})
    except Exception as e:
        print(e)
        return {'success': False, 'msg': e}
    finally:
        db.session.close()


@interface_debugging.route("/interface_debugging/delete_interface_test", methods=['delete'])
def delete_interface_test():
    try:
        request_body = request.json
        interface_test_id = request_body['id']
        obj = api_test.query.filter(api_test.id == interface_test_id).first()
        db.session.delete(obj)
        db.session.commit()
        # user = api_test.query.filter().all()
        return jsonify(
            {'code': 200, 'msg': '请求成功',
             'success': True})
    except Exception as e:
        print(e)
        return {'success': False, 'msg': e}
    finally:
        db.session.close()


@interface_debugging.route("/interface_debugging/interface_list", methods=['get'])
def select_interface_list():
    # 查询接口列表
    try:
        currentPage = request.args.get('current_page', 1)
        page_size = request.args.get('page_size', 10)
        methods = request.args.get('methods')
        id1 = request.args.get('id')
        name = request.args.get('name')
        # print(str(type(id1)) + '111111111111111111')
        # if name:
        #     query = api_test.query.filter(api_test.name == name)
        # else:
        #     query = api_test.query.filter()
        filter_list = []
        if methods:
            filter_list.append(or_(api_test.methods.like('%' + str(methods) + '%')))
        if name:
            filter_list.append(or_(api_test.name.like('%' + str(name) + '%')))
        if id1:
            filter_list.append(or_(api_test.id == id1))
        query = api_test.query.filter(
            # and_(api_test.methods.like('%'+str(methods)+'%'), api_test.name.like('%'+str(name)+'%')),
            # or_(api_test.name == name),
            # or_(api_test.methods.like('%' + str(methods) + '%')),
            # or_(api_test.name.like('%' + str(name) + '%')),
            # or_(api_test.id == int(id1), id1 == None)
            *filter_list
        )
        # query = api_test.query.filter(api_test.name)
        paginate = query.paginate(page=int(currentPage), per_page=int(page_size), error_out=False)
        interface_list = paginate.items
        # print(type(interface_list))
        current_page = paginate.page
        total_page = paginate.pages
        total = paginate.total
        from utils.database_func import model_to_dict
        interface_list = model_to_dict(interface_list)
        current_app.logger.error('1111111111111111')
        # total = len(query.all())
        # interface_list = api_test.query.filter().all()
        # return {'code':1}
        return jsonify(
            {'code': 200, 'msg': '请求成功',
             'success': True, 'data': interface_list, 'current_page': current_page, 'total_page': total_page,
             'total': total})
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'msg': e})
    finally:
        db.session.close()
