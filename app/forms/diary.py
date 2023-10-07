from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class DiaryCreateForm(FlaskForm):
    title = StringField(
        "Title", validators=[DataRequired()], render_kw={"placeholder": "Title", "autofocus": True}
    )
    content = TextAreaField(
        "Content", validators=[DataRequired()], render_kw={"placeholder": "Content"}
    )
    diary_date = StringField(
        "Date", validators=[DataRequired()], render_kw={"readonly": True}
    )

    submit = SubmitField("Submit")
