import json
from flask import Blueprint, jsonify
from flask import request
import requests as interface_request
from common.database import db, user_fung

interface_debugging = Blueprint("interface_debugging", __name__)


@interface_debugging.route("/interface_debugging/interface_test", methods=['POST'])
def interface_test():
    request_body = request.json
    methods = request_body['method']
    headers = request_body['headers']
    url = request_body['url']
    body = request_body['body']
    if methods == "post":
        res = interface_request.post(headers=headers, url=url, json=body)
        return res.text
    if methods == "get":
        print(url)
        res = interface_request.get(url=url)
        return jsonify(
            {'code': 20000, 'msg': '请求成功', 'data': {'code': int(res.status_code), 'elapsed': str(res.elapsed),'res':res.text},
             'success': True})
