
from werkzeug.exceptions import HTTPException

from app.exceptions.error import APIException

class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    status = 999

class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    status = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    status = 1001


class AuthFailed(APIException):
    code = 401
    status = 1005
    msg = 'authorization failed'


class Forbidden(APIException):
    code = 403
    status = 1004
    msg = 'forbidden, not in scope'
