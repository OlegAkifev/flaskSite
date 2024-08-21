from flask import Blueprint

report = Blueprint(
    'report',
    __name__,
    url_prefix='/report',
    static_folder='../static',
    template_folder='../templates',
)


@report.route('/')
def report_list():
    return 'Hello Report!'

