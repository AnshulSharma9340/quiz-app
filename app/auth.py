from flask import Blueprint, render_template, url_for, flash, session, redirect
from flask_login import login_user, logout_user, login_required, current_user

from app import db
from app.forms import RegistrationForm, LoginForm
from app.models import User

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("auth.profile"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            session["user_id"] = user.id
            session["score"] = 0
            return redirect(url_for("auth.profile"))
        flash("Incorrect email or password", "danger")
    return render_template("login.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    session.pop("user_id", None)
    session.pop("score", None)
    session.pop("start_time", None)
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("route.index"))


@bp.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("auth.profile"))

    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash("Email is already registered. Please choose a different one.", "danger")
            return redirect(url_for("auth.register"))

        if User.query.filter_by(username=form.username.data).first():
            flash("Username is already taken. Please choose a different one.", "danger")
            return redirect(url_for("auth.register"))

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You can now log in.", "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)
