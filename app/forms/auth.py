from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app.models.user import User


class RegisterForm(FlaskForm):
    full_name = StringField(
        "Full Name",
        validators=[DataRequired()],
        render_kw={"placeholder": "Full Name", "autofocus": True}
    )
    birthday = DateField(
        "Birthday", format="%Y-%m-%d", validators=[DataRequired()],
        render_kw={"placeholder": "Birthday"}
    )
    email = StringField(
        "E-Mail",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "E-Mail"}
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()], render_kw={"placeholder": "Password"}
    )
    password_confirm = PasswordField(
        "Password Confirm",
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"placeholder": "Password Confirm"}
    )
    submit = SubmitField("Register")

    def validate_email(self, email):  # noqa
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError("User is available.")


class LoginForm(FlaskForm):
    email = StringField(
        "E-Mail",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "E-Mail", "autofocus": True},
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()], render_kw={"placeholder": "Password"}
    )
    submit = SubmitField("Login")
