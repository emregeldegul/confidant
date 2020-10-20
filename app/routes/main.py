from flask import Blueprint, redirect, url_for, render_template
from flask_login import current_user, login_required

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
@main.route('/index')
@login_required
def index():
    return redirect(url_for('diary.index'))

@main.route('/test')
@login_required
def test():
    return 'ok'
