from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from ilexicon.api import register_blueprints


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dingshichen@127.0.0.1:3306/ilexicon'
    # 动态追踪修改设置，如未设置只会提示警告
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    return app