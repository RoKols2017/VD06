from flask import Blueprint, render_template
from app.forms import UserForm

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    form = UserForm()
    user_data = None

    if form.validate_on_submit():
        user_data = {
            "name": form.name.data,
            "city": form.city.data,
            "hobby": form.hobby.data,
            "age": form.age.data
        }

    return render_template("index.html", form=form, user_data=user_data)
