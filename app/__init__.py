from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app import auth, route
    app.register_blueprint(auth.bp)
    app.register_blueprint(route.bp)

    with app.app_context():
        db.create_all()
        from app.seed import seed_questions
        seed_questions()

    return app
