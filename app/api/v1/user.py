from flask import jsonify, g

from app.libs.error_code import DeleteSuccess, AuthFailed
from app.libs.redrprint import Redprint

# 注册红图
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')

# 管理员
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    # 高级知识：jsonify不能直接序列化对象，需要重写JSONEncoder的default
    return jsonify(user)

@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    # 高级知识：jsonify不能直接序列化对象，需要重写JSONEncoder的default
    return jsonify(user)


# 管理员
@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
    # 防止超权，从token中拿id
    # g变量是线程隔离的，多个用户访问delete不会出现错乱
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

# 普通用户, 只能删除自己的用户
@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    # 防止超权，从token中拿id
    # g变量是线程隔离的，多个用户访问delete不会出现错乱
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()

