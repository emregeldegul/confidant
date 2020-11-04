from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user

from app import db
from app.models.user import User
from app.forms.profile import PasswordEditForm, ProfileEditForm

profile = Blueprint('profile', __name__, url_prefix='/profile')

@profile.route('/')
@profile.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    profile_form = ProfileEditForm()
    password_form = PasswordEditForm()

    if profile_form.validate_on_submit():
        pass

    if password_form.validate_on_submit():
        user = User.query.filter(id = current_user.id).first()
        user.generate_password_hash(password_form.new)
        db.session.commit()

        flash('The Password was Changed', 'success')

    return render_template('views/profile/index.html',
        title = 'Edit Profile', profile_form = profile_form,
        password_form = password_form
    )
