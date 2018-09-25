from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        # 将post的json类型数据form化,静默模式，body没有参数时不会报异常
        data = request.get_json(silent=True)
        # 将get的参数Form化
        args = request.args.to_dict()
        super().__init__(data=data, **args)

    # 将wtform不抛出异常的特性，改为抛出异常的特性
    def validate_for_api(self):
        valid = super().validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
