from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown#flask包装的PageDown，把PageDown集成到Flask-WTF表单中

#由于尚未初始化所需的程序实例，所以没有初始化扩展，创建扩展类时没有向构造函数传入参数
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()
login_manager = LoginManager()

login_manager.session_protection = 'strong' #不同安全等级类型
login_manager.login_view = 'auth.login' #设置登录页面的端点


def create_app(config_name):#工厂函数
    app = Flask(__name__)
    app.config.from_object(config[config_name])#导入配置
    config[config_name].init_app(app)#初始化配置环境

    bootstrap.init_app(app)#这些都是程序初始化后的实例
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    pagedown.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint#导入蓝本
    app.register_blueprint(main_blueprint)#注册蓝本
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')#url_prefix使路由以/auth为前缀

    return app

