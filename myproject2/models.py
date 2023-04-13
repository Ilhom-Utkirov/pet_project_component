#models.py

from myproject2 import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin #library builtin attributes for login

#user loader decorator builtin decorator
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



#management features of login users and managing them
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    # if 2 users with same email and system sends  msg to restore password system gets confused
    email = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
