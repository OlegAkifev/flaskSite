from flask import Blueprint

user = Blueprint(
    'user',
    __name__,
    url_prefix='/users',
    static_folder='../static',
    template_folder='../templates'
    )


@user.route('/')
def user_list():
    return 'Hello User!'


@user.route('/<pk>')
def get_user(pk: int):
    return pk


