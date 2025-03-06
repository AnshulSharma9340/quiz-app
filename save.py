from app import db, create_app
from app import models

app = create_app()
with app.app_context():
    user = models.User(username = "Anshul",email = "anshulsharma7162@gmail.com")
    user.set_password("1234567890")
    db.session.add(user)
    db.session.commit()
