from datetime import datetime, timedelta, date
from json import loads

from flask import Blueprint, redirect, url_for, render_template, flash, jsonify
from flask_login import login_required, current_user

from app import db
from app.models.diary import Diary
from app.forms.diary import DiaryCreateForm

diary = Blueprint('diary', __name__, url_prefix='/diary')

@diary.route('/')
@diary.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return redirect(url_for('diary.show', date=date.today()))

@diary.route('/<date>', methods=['GET', 'POST'])
@login_required
def show(date):
    form = DiaryCreateForm()

    day = Diary.query.filter_by(user=current_user).filter_by(date=date).first()

    if form.validate_on_submit():
        pass

    nav_date = datetime.strptime(date, '%Y-%m-%d')

    navigation = {
        'previous': nav_date + timedelta(days=-1),
        'day': nav_date,
        'next': nav_date + timedelta(days=1)
    }

    if day:
        form.title.data = day.title
        form.content.data = day.content
        form.date.data = day.date

        title = "{}".format(day.title)
    else:
        title = "No Story Added for Today"

    return render_template('views/diary/show.html', title=title, form=form, navigation=navigation)

@diary.route('/create_or_update', methods=['POST'])
@login_required
def create_or_update():
    form = DiaryCreateForm()

    if not form.validate_on_submit():
        return jsonify({'status': 'error', 'form': form.errors})

    date = form.date.data

    day = Diary.query.filter_by(user=current_user).filter_by(date=date).first()

    if day:
        day.title = form.title.data
        day.content = form.content.data

        db.session.commit()

        return jsonify({'status': 'update'})
    else:
        print(form.date.data)
        print(type(form.date.data))
        diary = Diary(
            user = current_user,
            title = form.title.data,
            content = form.content.data,
            date = datetime.strptime(form.date.data, '%Y-%m-%d'),
        )

        db.session.add(diary)
        db.session.commit()

        return jsonify({'status': 'added'})

@diary.route('/diaries')
@login_required
def diaries():
    diaries = Diary.query.filter_by(user=current_user).all()
    return render_template('views/diary/diaries.html', title='All Diaries', diaries=diaries)
