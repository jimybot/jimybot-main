from sqlalchemy_api_handler import ApiErrors


def check_token(param, token):
    if 'token' not in param:
        errors = ApiErrors()
        errors.add_error('token', 'token is missing')
        raise errors

    if param['token'] != token:
        errors = ApiErrors()
        errors.add_error('token', 'not valid token')
        raise errors
