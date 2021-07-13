from flask import Blueprint, redirect, url_for
from flask_login import login_required

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
@main.route('/index')
@login_required
def index():
    return redirect(url_for('diary.index'))