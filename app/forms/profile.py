from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, length
from flask_login import current_user

from app.models.user import User

class ProfileEditForm(FlaskForm):
    name = StringField('Name',
        validators=[DataRequired()], render_kw={'placeholder': 'Name', 'autofocus': True}
    )
    birthday = DateField(
        'Birthday', format='%Y-%m-%d', validators=[DataRequired()],
        render_kw={'placeholder': 'Birthday'}
    )
    email = StringField(
        'E-Mail',
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'E-Mail'}
    )

    submit = SubmitField('Update')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()

        if user:
            raise ValidationError('User is available.')

class PasswordEditForm(FlaskForm):
    current = PasswordField('Current',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Curreny', 'autofocus': True}
    )
    new = PasswordField('New',
        validators=[DataRequired(), length(min=6)],
        render_kw={'placeholder': 'New'}
    )
    repeat_new = PasswordField('Re-Type New',
        validators=[DataRequired(), EqualTo('new'), length(min=6)],
        render_kw={'placeholder': 'Re-Type New'}
    )

    submit = SubmitField('Update')

    def validate_current(self, current):
        user = User.query.filter_by(id = current_user.id).first()

        if not user.check_password(current.data):
            raise ValidationError('Wrong Password')
