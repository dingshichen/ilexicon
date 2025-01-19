from abc import abstractmethod, ABCMeta
from enum import Enum
from typing import TypeVar, Generic

T = TypeVar("T")


class ResultStatus(Enum):
    SUCCESS = 0, "success"
    FAIL = -1, "fail"
    SYSTEM_ERROR = -1000, "系统错误"
    ENTITY_NOT_FOUND = -1011, "数据不存在"
    PARAM_ERROR = -1012, "参数错误"

    def __init__(self, code: int, desc: str):
        self._code = code
        self._desc = desc

    @property
    def code(self):
        return self._code

    @property
    def desc(self):
        return self._desc


class ApiModel(metaclass=ABCMeta):

    @abstractmethod
    def as_dict(self) -> dict:
        return {}


# 结果
class Result(ApiModel, Generic[T]):
    code: int
    message: str
    data: T | None

    def __init__(self, code: int, message: str, data: T | None = None):
        self.code = code
        self.message = message
        self.data = data

    @classmethod
    def success(cls, data: T | None = None):
        return Result(code=ResultStatus.SUCCESS.code, message=ResultStatus.SUCCESS.desc, data=data)

    @classmethod
    def fail(cls, code: int, message: str):
        return Result(code=code, message=message)

    def as_dict(self):
        return {"code": self.code, "message": self.message, "data": self.data}

