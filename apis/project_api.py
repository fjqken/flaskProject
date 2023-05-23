from flask import Blueprint, jsonify
from flask import request

project_api = Blueprint("project_api", __name__)


@project_api.route("/project_api/creat", methods=['POST'])
def creat_project():
    return jsonify({
        "tableData": [{
            "date": '2016-05-02',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1518 弄'
        }, {
            "date": '2016-05-04',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1517 弄'
        }, {
            "date": '2016-05-01',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1519 弄'
        }, {
            "date": '2016-05-03',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1516 弄'
        }],
        "total": 0,
        "pageSize": 10,
        "currentPage": 1
    })
