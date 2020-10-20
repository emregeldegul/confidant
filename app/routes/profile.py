from flask import Blueprint, render_template
from flask_login import login_required

profile = Blueprint('profile', __name__, url_prefix='/profile')

@profile.route('/')
@profile.route('/index')
@login_required
def index():
    return render_template('views/profile/index.html', title = 'Edit Profile')

@profile.route('/password')
@login_required
def password():
    return render_template('views/profile/password.html', title = 'Edit Password')
