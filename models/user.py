import uuid
from common.database import UserDatabase


class User:
    collection = 'users'

    def __init__(self, username, password, email, _id=None):
        self.username = username
        self.password = password
        self.email = email
        self._id = _id or uuid.uuid4().hex

    def get_user_data(self):
        return {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            '_id': self._id
        }


    def save_to_mongo(self):
        UserDatabase.insert(self.collection, self.get_user_data())


user = User('Adi', '651465', 'adi@gmail.com')
user.save_to_mongo()
