from datetime import datetime
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, SmallInteger, Integer

# 高级用法，继承父类的Query,改写filter_by,以后的查询都会有status
from app.libs.error_code import NotFound


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        # 取字典中的所有key
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv



#contextmanager的高级用法
class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

db = SQLAlchemy(query_class=Query)

class Base(db.Model):
    # 设置为True是为了告诉Flask不用创建Base这张表
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    # 实用方法，将user对象序列化成dict时，会调用这个方法
    def keys(self):
        return self.fields

    # 实现隐藏模型的某些字段，减少post或者get时的一些带宽
    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    # 使用dict(user)时，为保证可以使用user['id']拿到id时，需要调用这个方法
    def __getitem__(self, item):
        return getattr(self, item)

    # 高级用法，如果字典中有和Model中相同名字的key，则自动赋值
    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self,key) and key != 'id':
                setattr(self,key,value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    # 软删除
    def delete(self):
        self.status = 0



