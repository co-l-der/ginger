from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

# 高级用法，使Jsonify可以直接序列化对象
from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        # o.__dict__只能将o中的实例变量转成字典，类变量无法转换
        # return o.__dict__
        # 需要重写对象中的keys和__getitem__方法，才能实现调用o['key']
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()

# 用自己定义的JSONEncoder代替原来的JSONEncoder
class Flask(_Flask):
    json_encoder = JSONEncoder