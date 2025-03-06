from flask import Blueprint, g,render_template, url_for, flash,session, redirect, request
from flask_login import login_user, logout_user, login_required
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app import db
bp = Blueprint("auth",__name__)

@bp.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = User.query.filter_by(id = session['user_id']).first()

        g.user = user

@bp.route("/login", methods = ["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        # if user is None:
        #     flash("Account does not exit")
        #     return render_template("login.html", form = form)
        # if not user.check_password(form.password.data):
        #     flash("Incorrect password")
        if user and user.check_password(form.password.data):
            login_user(user)
            session['user_id'] = user.id
            session['score'] = 0
 
            return render_template("profile.html", user = user)
            # return redirect(url_for("route.question", id = 1))
        else:
            flash("Incorrect password or username")
    return render_template("login.html", form = form)


@bp.route("/logout")
def logout():
    session.pop('user_id', None)
    session.pop('score', None)
    logout_user()
    return render_template("index.html")

@bp.route("/register", methods = ["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # check for register email
        exiting_email = User.query.filter_by(email = form.email.data).first()

        if exiting_email:
            flash('Email is already registered. Please choose a different one.', 'danger')
            return redirect(url_for('auth.register'))
        # checking if the username exit
        existing_username = User.query.filter_by(username=form.username.data).first()
        if existing_username:
            flash('Username is already taken. Please choose a different one.', 'danger')
            return redirect(url_for('auth.register'))
        user = User( username = form.username.data, 
                    email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template("register.html", form = form)

@bp.route("/profile")
@login_required
def profile():
    if g.user:
        score = request.args.get('score')
        g.score = score
        return render_template("profile.html", user = g.user)