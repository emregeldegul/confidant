from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_user, logout_user, current_user

from app.models.user import User
from app.forms.auth import RegisterForm, LoginForm

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/")
@auth_bp.route("/index")
def index():
    return redirect(url_for("auth.login"))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            full_name=form.full_name.data,  # noqa
            email=form.email.data,  # noqa
            birthday=form.birthday.data  # noqa
        )
        user.generate_password_hash(form.password.data)
        user.save()
        login_user(user)
        flash("Successful! Now You Can Add Your Thoughts Here.", "success")
        return redirect(url_for("main.index"))

    return render_template("views/auth/register.html", title="Register", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Login Failed.", "danger")
        else:
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main.index"))

    return render_template("views/auth/login.html", title="Login", form=form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("Logged Out.", "success")
    return redirect(url_for("auth.login"))
