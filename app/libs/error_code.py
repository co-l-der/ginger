from werkzeug.exceptions import HTTPException

# 继承werkzeug的HTTPException
from app.libs.error import APIException

class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake'
    error_code = 999

class Success(APIException):
    code=201
    msg='ok'
    error_code=0

class DeleteSuccess(Success):
    code = 202
    error_code = 1

class ClientTypeError(APIException):
    # 400,请求参数错误
    code = 400
    msg = 'client is invalid'
    error_code = 1006

class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000

class NotFound(APIException):
    code = 404
    msg = 'the resource are not found'
    error_code = 1001

# 授权失败
class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'

# 禁止访问
class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'
