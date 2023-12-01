import json
from datetime import datetime, date
from flask_sqlalchemy import Model

# from models.database_func import model_to_dict


class ComplexEncoder(json.JSONEncoder):
    """
    含有 datetime 对象数据转 json 时，时间格式会报错
    """

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        # elif isinstance(obj, Model):
        #     return model_to_dict(obj)
        elif isinstance(obj, object):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)

