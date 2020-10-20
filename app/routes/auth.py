from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_user, logout_user, current_user

from app import db
from app.models.user import User
from app.forms.auth import RegisterForm, LoginForm

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/')
@auth.route('/index')
def index():
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data,
            birthday=form.birthday.data
        )

        user.generate_password_hash(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Successful! You Can Login.', 'success')

    return render_template('views/auth/register.html', title='Register', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Login Failed', 'danger')
        else:
            login_user(user)

            next = request.args.get('next')

            return redirect(next or url_for('main.index'))

    return render_template('views/auth/login.html', title='Login', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('Logged Out', 'success')
    return redirect(url_for('auth.login'))
