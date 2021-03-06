from flask_login import UserMixin
from .extensions import mongo
import uuid


# Uses this class to log in a User, pulls fields form database for use in
# dynamic content
class User(UserMixin):
    def __init__(self, user_id, username, password, prefill, liked, _id=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.prefill = prefill
        self.liked = liked
        self._id = uuid.uuid4().hex if _id is None else _id

    # Below is necessary functionality for flask-login
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self._id)

    @classmethod
    def get_by_id(cls, _id):
        data = mongo.db.users.find_one({"_id": _id})
        if data is not None:
            return cls(**data)
