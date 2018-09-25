
from app.libs.redrprint import Redprint

# 注册红图
api = Redprint('book')

@api.route('', methods=['GET'])
def get_book():
    return "get_book"

@api.route('', methods=['GET'])
def create_book():
    return "create_book"