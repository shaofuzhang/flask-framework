from flask.blueprints import Blueprint
from flask import render_template, jsonify
from models.baseModel import db

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
    return jsonify({"a": "测试"})
    # return render_template('home/index.html')