from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user

from app import db
from app.models.user import User
from app.forms.profile import PasswordEditForm, ProfileEditForm

profile_bp = Blueprint("profile", __name__, url_prefix="/profile")


@profile_bp.route("/")
@profile_bp.route("/index")
@login_required
def index():
    user = User.query.filter_by(id=current_user.id).first()

    profile_form = ProfileEditForm()
    password_form = PasswordEditForm()

    profile_form.full_name.data = user.full_name
    profile_form.birthday.data = user.birthday
    profile_form.email.data = user.email

    return render_template(
        "views/profile/index.html",
        title="Edit Profile", profile_form=profile_form, password_form=password_form
    )


@profile_bp.route("/edit", methods=["POST"])
@login_required
def edit():
    profile_form = ProfileEditForm()
    user = User.query.filter_by(id=current_user.id).first()

    if not profile_form.validate_on_submit():
        return jsonify({"status": "error", "form": profile_form.errors})

    user.full_name = profile_form.full_name.data
    user.birthday = profile_form.birthday.data
    user.email = profile_form.email.data
    user.save()

    return jsonify({"status": "success"})


@profile_bp.route("/password", methods=["POST"])
@login_required
def password():
    password_form = PasswordEditForm()
    user = User.query.filter_by(id=current_user.id).first()

    if not password_form.validate_on_submit():
        return jsonify({"status": "error", "form": password_form.errors})

    user.generate_password_hash(password_form.new.data)
    user.save()

    return jsonify({"status": "success"})
