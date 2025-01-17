from ilexicon import ResultStatus


class ApiException(Exception):
    errno: int
    message: str

    def __init__(self, errno: int, message: str):
        self.errno = errno
        self.message = message


class EntityNotFoundException(ApiException):

    def __init__(self, message: str | None):
        super().__init__(ResultStatus.ENTITY_NOT_FOUND.code, message if message else ResultStatus.ENTITY_NOT_FOUND.desc)