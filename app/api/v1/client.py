from flask import request

from app.libs.error_code import Success
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.libs.redrprint import Redprint

api = Redprint('client')

@api.route('/register', methods=['POST'])
def create_client():
    # 解决已知异常和未知异常，AOP思想，出口堵住所以未知异常
    # 将提交为json格式的数据转换成Form形式进行验证,所有的参数要从form中拿到做验证
    form = ClientForm()
    form.validate_for_api()
    # 实现switch-case
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email,
    }
    promise[form.type.data]()
    return Success()
    # 注册 登录
    # 参数 校验 接收参数
    # WTFrom 验证表单
    pass

def __register_user_by_email():
    form = UserEmailForm()
    form.validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)