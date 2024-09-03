from flask import Blueprint, render_template

report = Blueprint(
    'report',
    __name__,
    url_prefix='/reports',
    static_folder='../static',
    template_folder='../templates',
)


@report.route('/')
def report_list():
    return render_template('report/list.html', reports=[1, 2, 3, 4, 5])

