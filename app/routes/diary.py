from datetime import datetime, timedelta, date
from json import loads

from flask import Blueprint, redirect, url_for, render_template, flash, jsonify
from flask_login import login_required, current_user

from app import db
from app.models.diary import Diary
from app.forms.diary import DiaryCreateForm

diary = Blueprint('diary', __name__, url_prefix='/diary')

@diary.route('/')
@diary.route('/index')
@login_required
def index():
    return redirect(url_for('diary.show', date=date.today()))

@diary.route('/<date>', methods=['GET', 'POST'])
@login_required
def show(date):
    form = DiaryCreateForm()

    day = Diary.query.filter_by(user=current_user).filter_by(date=date).first()

    nav_date = datetime.strptime(date, '%Y-%m-%d')

    navigation = {
        'previous': nav_date + timedelta(days=-1),
        'day': nav_date,
        'next': nav_date + timedelta(days=1)
    }

    if day:
        form.title.data = day.show_title()
        form.content.data = day.show_content()
        form.date.data = day.date

        title = "{}".format(day.show_title())
    else:
        title = "No Story Added for Today"

    return render_template('views/diary/show.html', title=title, form=form, navigation=navigation)

@diary.route('/create_or_update', methods=['POST'])
@login_required
def create_or_update():
    form = DiaryCreateForm()

    if not form.validate_on_submit():
        return jsonify({'status': 'error', 'form': form.errors}), 400

    date = form.date.data
    day = Diary.query.filter_by(user=current_user).filter_by(date=date).first()

    if day:
        day.save_title(form.title.data)
        day.save_content(form.content.data)

        db.session.commit()

        return jsonify({'status': 'update'})
    else:
        diary = Diary(
            user = current_user,
            date = datetime.strptime(form.date.data, '%Y-%m-%d'),
        )

        diary.save_title(form.title.data)
        diary.save_content(form.content.data)

        db.session.add(diary)
        db.session.commit()

        return jsonify({'status': 'added'})

@diary.route('/diaries')
@login_required
def diaries():
    diaries = Diary.query.filter_by(user=current_user).all()
    return render_template('views/diary/diaries.html', title='All Diaries', diaries=diaries)
