from datetime import datetime, timedelta, date

from flask import Blueprint, redirect, url_for, render_template, jsonify
from flask import request
from flask_login import login_required, current_user

from app.models.diary import Diary
from app.forms.diary import DiaryCreateForm

from app.helpers.search_helper import SearchHelper

diary_bp = Blueprint("diary", __name__, url_prefix="/diary")


@diary_bp.route("/")
@diary_bp.route("/index")
@login_required
def index():
    return redirect(url_for("diary.get_diary", diary_date=date.today()))


@diary_bp.route("/diaries")
@login_required
def all_diaries():
    diaries = Diary.query.filter_by(user=current_user).all()
    return render_template("views/diary/all_diaries.html", title="All Diaries", diaries=diaries)


@diary_bp.route("/create", methods=["POST"])
@login_required
def create_diary():
    form = DiaryCreateForm()

    if not form.validate_on_submit():
        return jsonify({"status": "error", "form": form.errors}), 400

    diary_date = form.diary_date.data
    diary = Diary.query.filter_by(user=current_user).filter_by(diary_date=diary_date).first()

    if diary:
        diary.save_title(form.title.data)
        diary.save_content(form.content.data)
        diary.save()
        return jsonify({"status": "update"})
    else:
        diary = Diary(user=current_user, diary_date=datetime.strptime(form.diary_date.data, "%Y-%m-%d"))
        diary.save_title(form.title.data)
        diary.save_content(form.content.data)
        diary.save()
        return jsonify({"status": "added"})


@diary_bp.route("/search", methods=["POST"])
@login_required
def search():
    # Fetch form details
    search_string = request.form.get("search_string")

    # Tokenize search_string by removing whitespace characters
    keywords = search_string.split()

    the_diaries = Diary.query.filter_by(user=current_user).all()
    se = SearchHelper(the_diaries)
    results = se.search(keywords)

    return render_template(
        "views/diary/search-results.html",
        title="Search Results",
        diaries=results,
        search_string=search_string
    )


@diary_bp.route("/<string:diary_date>", methods=["GET"])
@login_required
def get_diary(diary_date: str):
    form = DiaryCreateForm()
    diary = Diary.query.filter_by(user=current_user).filter_by(diary_date=diary_date).first()
    nav_date = datetime.strptime(diary_date, "%Y-%m-%d")
    navigation = {"previous": nav_date + timedelta(days=-1), "day": nav_date, "next": nav_date + timedelta(days=1)}

    if diary:
        form.title.data = diary.show_title()
        form.content.data = diary.show_content()
        form.diary_date.data = diary.diary_date
        title = "{}".format(diary.show_title())
    else:
        title = "No Story Added for Today"

    return render_template("views/diary/show.html", title=title, form=form, navigation=navigation)
