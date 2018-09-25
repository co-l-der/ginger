"""
用户权限
"""

class Scope:
    allow_api = []
    allow_module = []
    firbidden = []
    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        # 运算符重载, 实现+的行为
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))
        return self

class AdminScope(Scope):
    allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']
    #allow_module = ['v1.user']

    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    allow_api = ['v1.user+get_user', 'v1.user+delete_user']


def is_in_scope(scope, endpoint):
    # python 将当前模块中的所有变量和类变成字典存放在globals中
    # 反射,从拿到一个类的名字，可以实例化这个类的对象
    # gl = globals()
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.firbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False

