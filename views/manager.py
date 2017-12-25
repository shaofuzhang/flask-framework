from flask.blueprints import Blueprint
from flask import render_template

bp = Blueprint('manager', __name__)


@bp.route('/')
@bp.route('/login')
def login():
    return render_template('manager/login.html')


@bp.route('/index')
def index():
    return render_template('manager/index.html')