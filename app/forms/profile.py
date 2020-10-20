from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

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
