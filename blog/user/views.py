from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

user = Blueprint(
    'user',
    __name__,
    url_prefix='/users',
    static_folder='../static',
    template_folder='../templates'
    )

USERS = {
    1: 'Alice',
    2: 'John',
    3: 'Bob',
    4: 'Dave',
    5: 'Eve',
    6: 'Mike',
}


@user.route('/')
def user_list():
    return render_template('users/list.html', users=USERS)


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        # raise NotFound(f'User_id {pk} does not exist')
        return redirect('/users/')
    return render_template('users/details.html', user_name=user_name)
