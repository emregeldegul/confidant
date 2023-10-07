from flask import Blueprint, redirect, url_for
from flask_login import login_required

main_bp = Blueprint("main", __name__, url_prefix="/")


@main_bp.route("/")
@main_bp.route("/index")
@login_required
def index():
    return redirect(url_for("diary.index"))
