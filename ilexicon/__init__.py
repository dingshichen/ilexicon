import json
from datetime import datetime, date, time
from decimal import Decimal
from enum import Enum

from flask import Flask, typing as ft, Response
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.pagination import Pagination

from ilexicon.api import register_blueprints
from ilexicon.base import Result, ApiModel, ResultStatus
from ilexicon.exception import ApiException

db = SQLAlchemy()

class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(o, date):
            return o.strftime("%Y-%m-%d")
        if isinstance(o, time):
            return o.strftime("%H:%M:%S")
        if isinstance(o, Enum):
            return o.value
        if isinstance(o, bytes):
            o = o.decode("utf-8")
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)

class ApiFlask(Flask):

    def make_response(self, rv: ft.ResponseReturnValue) -> Response:
        if rv is None:
            res = Result.success()
        elif isinstance(rv, dict):
            res = Result.success(rv)
        elif isinstance(rv, list):
            res = Result.success(rv)
        elif isinstance(rv, tuple):
            res = Result.success(rv)
        elif isinstance(rv, Pagination):
            res = Result.success({
                "pages": rv.pages,
                "hasPrev": rv.has_prev,
                "hasNext": rv.has_next,
                "total": rv.total,
                "list": [item.as_dict() for item in rv.items],
            })
        elif isinstance(rv, ApiModel):
            res = Result.success(rv.as_dict())
        elif isinstance(rv, ApiException):
            res = Result.fail(rv.errno, rv.message)
        elif isinstance(rv, Exception):
            res = Result.fail(ResultStatus.SYSTEM_ERROR.code, ResultStatus.SYSTEM_ERROR.desc)
        else:
            res = None
        if res is None:
            return super().make_response(rv)
        else:
            # TODO 不展示 null 值的 key
            return Response(
                json.dumps(res.as_dict(), ensure_ascii=False, cls=JsonEncoder),
                status=200,
                mimetype="application/json",
            )


def create_app():
    app = ApiFlask(__name__)
    register_blueprints(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dingshichen@127.0.0.1:3306/ilexicon'
    # 动态追踪修改设置，如未设置只会提示警告
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    return app