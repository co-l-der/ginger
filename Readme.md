**代码实现步骤**
1.路由的设计，蓝图的注册，红图的设计和注册
2.json标准形式的返回
3.已知异常和未知异常的捕捉和返回
4.用户登录后Token的生成和返回：写令牌在token.py；读令牌token_auth.py
5，用户权限控制，scope
6.验证令牌

POST和GET的区别：
当请求需要带参数时
1.post将请求的参数放在body中
2.get是将请求的参数直接放在url后面，以问号分隔

面试问题：
**Restful接口在进行用户登录时使用HTTPBasicAuth发送账户和密码
是将用户信息放在请求头中传递的，而且需要做Base64编码**

**关于元类的用法**
SQLAchemy使用元类创建的对象，并不会执行模型函数中的构造函数


**功能**
client.py POST方式注册用户功能，提供3种不同注册方式，不同于表单注册
user.py 提供用户查询和删除的功能，并设置两种用户权限，在验证用户Token时，需要将用户信息放在请求头中或使用HTTPBasicAuth
token.py 提供根据用户生成token，和根据token查询用户id的功能
error.py 提供了统一返回的json格式
error_code.py 提供放回统一的异常的json格式


**重要知识**
1.Blueprint和自定义Redprint,endpoint，路由的设计
2.重写HTTPException，定义自己的APIException，error_code
3.将post的json参数form化，将get方法提交的参数form化
3.重写Form的validate，使之将error可以当做异常抛出
4.当出现未知异常时，使用AOP思想，在出口统一做一个Exception的判别，使用@app.errorhandler(Exception)
5.将对象序列化成dict时，需要在model中重写keys和__getitem__()方法
6.将字典转成对象调用时，需要使用nametuple
7.使用g变量，保存当前用户信息，可以做到线程隔离
8.scope做权限控制
9.ORM在创建对象时是使用的元类，如果想调用构造方法，则需要使用@orm.reconstructor，
可以用在隐藏模型的某个字段场景，见models中user.py，避免建立多个视图模型

**难点：**
1.路由的设计
2.json标准化返回
3.异常如何标准化成json
4.用户权限如何控制


