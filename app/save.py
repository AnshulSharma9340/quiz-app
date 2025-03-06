from app import db
from john import models


user1 = User("Anshul","anshulsharma7162@gmail.com")

db.session.add(user)
db.session.commit()