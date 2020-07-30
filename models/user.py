import uuid
from common.mongo_stock_db import UserDatabase


class User:
    collection = 'users'

    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = _id or uuid.uuid4().hex

    def get_user_data(self):
        return {
            'password': self.password,
            'email': self.email,
            '_id': self._id
        }


    def save_to_mongo(self):
        UserDatabase.insert(self.collection, self.get_user_data())


